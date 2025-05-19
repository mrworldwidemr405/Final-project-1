from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QRadioButton,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QButtonGroup, QTextEdit
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from logic import already_voted, save_vote, load_votes


class VotingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voting App")
        self.setFixedSize(350, 400)
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.vote_screen()

    def clear(self):
        while self.layout.count():
            thing = self.layout.takeAt(0)
            if thing.widget():
                thing.widget().deleteLater()

    def vote_screen(self):
        self.clear()
        title = QLabel("VOTING APP")
        title.setFont(QFont("Arial", 14))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(title)

        id_row = QHBoxLayout()
        id_row.addWidget(QLabel("ID:"))
        self.id_box = QLineEdit()
        id_row.addWidget(self.id_box)
        self.layout.addLayout(id_row)

        self.layout.addWidget(QLabel("Pick One:", alignment=Qt.AlignmentFlag.AlignCenter))

        self.b = QRadioButton("Bianca")
        self.e = QRadioButton("Edward")
        self.f = QRadioButton("Felicia")

        self.group = QButtonGroup()
        for btn in [self.b, self.e, self.f]:
            self.group.addButton(btn)
            self.layout.addWidget(btn)

        submit = QPushButton("Vote")
        submit.clicked.connect(self.do_vote)
        self.layout.addWidget(submit)

        view = QPushButton("View Votes")
        view.clicked.connect(self.show_votes)
        self.layout.addWidget(view)

        self.msg = QLabel("")
        self.msg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.msg)

    def do_vote(self):
        uid = self.id_box.text().strip()
        if uid == "":
            self.show_msg("Need ID", "red")
            return

        if already_voted(uid):
            self.show_msg("You already voted", "red")
            return

        if self.b.isChecked():
            name = "Bianca"
        elif self.e.isChecked():
            name = "Edward"
        elif self.f.isChecked():
            name = "Felicia"
        else:
            self.show_msg("Pick someone", "red")
            return

        save_vote(uid, name)
        self.show_msg("Vote saved!", "green")
        self.id_box.clear()
        self.group.setExclusive(False)
        for btn in [self.b, self.e, self.f]:
            btn.setChecked(False)
        self.group.setExclusive(True)

    def show_msg(self, text, color):
        self.msg.setText(text)
        self.msg.setStyleSheet(f"color: {color}; font-weight: bold;")

    def show_votes(self):
        self.clear()
        title = QLabel("VOTE HISTORY")
        title.setFont(QFont("Arial", 12))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        box = QTextEdit()
        box.setReadOnly(True)
        box.setText(load_votes())

        back = QPushButton("Back")
        back.clicked.connect(self.vote_screen)

        self.layout.addWidget(title)
        self.layout.addWidget(box)
        self.layout.addWidget(back)