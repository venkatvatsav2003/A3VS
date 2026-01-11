from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from scanner.nmap_runner import run_nmap
from scanner.progress_tracker import estimate_progress
from scanner.auth_scanner import build_auth_args
from config.scan_profiles import SCAN_PROFILES
from ai.report_generator import generate_ai_report

class ScanThread(QThread):
    output_signal = pyqtSignal(str)
    progress_signal = pyqtSignal(int)
    finished_signal = pyqtSignal(str)

    def __init__(self, command):
        super().__init__()
        self.command = command
        self.raw_output = ""

    def run(self):
        def on_output(line):
            self.raw_output += line
            self.output_signal.emit(line)
            progress = estimate_progress(line)
            if progress != -1:
                self.progress_signal.emit(progress)

        run_nmap(self.command, on_output)
        self.finished_signal.emit(self.raw_output)

class A3VSGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A3VS – AI Vulnerability Scanner")
        self.setGeometry(200, 100, 900, 700)

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.target = QLineEdit()
        self.target.setPlaceholderText("Target IP / Domain")
        layout.addWidget(self.target)

        self.scan_type = QComboBox()
        self.scan_type.addItems(SCAN_PROFILES.keys())
        layout.addWidget(self.scan_type)

        self.user = QLineEdit()
        self.user.setPlaceholderText("Username (optional)")
        layout.addWidget(self.user)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password (optional)")
        self.password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password)

        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        btn = QPushButton("Start Scan")
        btn.clicked.connect(self.start_scan)
        layout.addWidget(btn)

    def start_scan(self):
        target = self.target.text().replace("http://", "").replace("https://", "").strip("/")
        scan_cmd = SCAN_PROFILES[self.scan_type.currentText()]
        auth = build_auth_args(self.user.text(), self.password.text())

        command = f"nmap {scan_cmd} {auth} {target}"

        self.thread = ScanThread(command)
        self.thread.output_signal.connect(self.output.append)
        self.thread.progress_signal.connect(self.progress.setValue)
        self.thread.finished_signal.connect(self.generate_report)
        self.thread.start()

    def generate_report(self, raw_output):
        with open("reports/raw_scan.txt", "w") as f:
            f.write(raw_output)

        report = generate_ai_report(raw_output)

        with open("reports/final_report.md", "w") as f:
            f.write(report)

        QMessageBox.information(self, "Scan Complete", "AI Report Generated!")
