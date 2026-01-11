import sys
from PyQt5.QtWidgets import QApplication
from gui.main_gui import A3VSGUI

app = QApplication(sys.argv)
window = A3VSGUI()
window.show()
sys.exit(app.exec_())
