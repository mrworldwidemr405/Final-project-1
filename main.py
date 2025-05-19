import sys
from gui import VotingApp
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
win = VotingApp()
win.show()
sys.exit(app.exec())