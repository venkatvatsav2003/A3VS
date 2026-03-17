import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QFont, QIcon
from scanner.nmap_runner import run_nmap
from scanner.progress_tracker import estimate_progress
from scanner.auth_scanner import build_auth_args
from config.scan_profiles import SCAN_PROFILES
from ai.report_generator import generate_ai_report
from utils.logger import logger
from utils.reporter_pdf import generate_pdf_report

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

class ReportThread(QThread):
    finished_signal = pyqtSignal(str)

    def __init__(self, raw_output):
        super().__init__()
        self.raw_output = raw_output

    def run(self):
        report = generate_ai_report(self.raw_output)
        self.finished_signal.emit(report)

class A3VSGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A3VS – AI Vulnerability Scanner")
        self.setGeometry(200, 100, 1000, 800)
        self.setAcceptDrops(True)
        
        # Ensure reports directory exists
        os.makedirs("reports", exist_ok=True)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Header
        header = QLabel("🛡️ A3VS - Advanced Vulnerability Scanner")
        header.setFont(QFont("Arial", 16, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # Form
        form_layout = QFormLayout()
        self.target = QLineEdit()
        self.target.setPlaceholderText("e.g., 192.168.1.1 or example.com")
        form_layout.addRow("Target IP / Domain:", self.target)

        self.scan_type = QComboBox()
        self.scan_type.addItems(SCAN_PROFILES.keys())
        form_layout.addRow("Scan Profile:", self.scan_type)

        self.user = QLineEdit()
        self.user.setPlaceholderText("SSH/Web Username (optional)")
        form_layout.addRow("Auth Username:", self.user)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password (optional)")
        self.password.setEchoMode(QLineEdit.Password)
        form_layout.addRow("Auth Password:", self.password)

        layout.addLayout(form_layout)

        # Progress bar
        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        # Output console
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setFont(QFont("Courier New", 10))
        self.output.setStyleSheet("background-color: #1e1e1e; color: #d4d4d4;")
        layout.addWidget(self.output)

        # Actions
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("🚀 Start Scan")
        self.start_btn.setMinimumHeight(40)
        self.start_btn.clicked.connect(self.start_scan)
        btn_layout.addWidget(self.start_btn)

        self.clear_btn = QPushButton("🧹 Clear Log")
        self.clear_btn.clicked.connect(self.output.clear)
        btn_layout.addWidget(self.clear_btn)
        
        layout.addLayout(btn_layout)

        self.statusBar().showMessage("Ready")

    def start_scan(self):
        target = self.target.text().strip()
        if not target:
            QMessageBox.warning(self, "Validation Error", "Target cannot be empty.")
            return

        # Sanitize target (basic)
        target = target.replace("http://", "").replace("https://", "").strip("/")
        
        scan_cmd = SCAN_PROFILES[self.scan_type.currentText()]
        auth = build_auth_args(self.user.text(), self.password.text())

        command = f"nmap {scan_cmd} {auth} {target}"

        self.start_btn.setEnabled(False)
        self.output.append(f"<b>Initiating scan: {command}</b><br>")
        self.statusBar().showMessage("Scanning in progress...")
        self.progress.setValue(0)

        self.thread = ScanThread(command)
        self.thread.output_signal.connect(self.output.append)
        self.thread.progress_signal.connect(self.progress.setValue)
        self.thread.finished_signal.connect(self.on_scan_finished)
        self.thread.start()

    def on_scan_finished(self, raw_output):
        self.progress.setValue(100)
        self.statusBar().showMessage("Scan complete. Generating AI Report...")
        
        try:
            with open("reports/raw_scan.txt", "w") as f:
                f.write(raw_output)
        except Exception as e:
            logger.error(f"Failed to write raw scan to file: {e}")

        # Start report thread
        self.report_thread = ReportThread(raw_output)
        self.report_thread.finished_signal.connect(self.on_report_finished)
        self.report_thread.start()

    def on_report_finished(self, report):
        try:
            with open("reports/final_report.md", "w") as f:
                f.write(report)
            
            # Generate PDF
            generate_pdf_report(report, "reports/final_report.pdf")
        except Exception as e:
            logger.error(f"Failed to write AI report or generate PDF: {e}")

        self.start_btn.setEnabled(True)
        self.statusBar().showMessage("All tasks completed.")
        QMessageBox.information(self, "Task Completed", "AI Vulnerability Report has been generated in reports/final_report.md and reports/final_report.pdf")
