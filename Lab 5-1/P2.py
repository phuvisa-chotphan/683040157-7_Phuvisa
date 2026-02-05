"""
Phuvisa Chotphan
683040157-7
P2
"""

import sys
from PySide6.QtWidgets import (QApplication, QMainWindow ,QTextEdit, QVBoxLayout, QWidget, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QDateEdit, QButtonGroup, QRadioButton, QComboBox, QCheckBox)
from PySide6.QtCore import Qt, QDate

class StudentRegistration(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(25, 20, 25, 20)

        # Title
        title = QLabel("Student Registration Form")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size:18px; font-weight:bold;")
        main_layout.addWidget(title)

        main_layout.addSpacing(15)

        # FormLayout 
        form_layout = QFormLayout()
        form_layout.setVerticalSpacing(5)

        # Full Name
        self.name_input = QLineEdit()
        label1 = QLabel("Fullname:")
        form_layout.addRow(label1)
        form_layout.addRow(self.name_input)

        # Email
        self.email_input = QLineEdit()
        label2 = QLabel("Email:")
        form_layout.addRow(label2)
        form_layout.addRow(self.email_input)

        # Phone
        self.phone_input = QLineEdit()
        label3 = QLabel("Phone:")
        form_layout.addRow(label3)
        form_layout.addRow(self.phone_input)

        # Date of Birth
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_edit.setDate(QDate(2000, 1, 1))

        label4 = QLabel("Date of Birth (dd/MM/yyyy):")
        form_layout.addRow(label4)
        form_layout.addRow(self.date_edit)

        # Gender
        gender_layout = QHBoxLayout()

        self.gender_group = QButtonGroup(self)

        self.male = QRadioButton("Male")
        self.female = QRadioButton("Female")
        self.nonbinary = QRadioButton("Non-binary")
        self.prefer = QRadioButton("Prefer not to say")

        self.gender_group.addButton(self.male)
        self.gender_group.addButton(self.female)
        self.gender_group.addButton(self.nonbinary)
        self.gender_group.addButton(self.prefer)

        gender_layout.addWidget(self.male)
        gender_layout.addWidget(self.female)
        gender_layout.addWidget(self.nonbinary)
        gender_layout.addWidget(self.prefer)

        label5 = QLabel("Gender:")
        form_layout.addRow(label5)
        form_layout.addRow(gender_layout)

        # Program
        self.program_combo = QComboBox()

        self.program_combo.addItem("Select your program")

        programs = [
            "Computer Engineering",
            "Digital Media Engineering",
            "Environmental Engineering",
            "Electical Engineering",
            "Semiconductor Engineering",
            "Mechanical Engineering",
            "Industrial Engineering",
            "Logistic Engineering",
            "Power Engineering",
            "Electronic Engineering",
            "Telecommunication Engineering",
            "Agricultural Engineering",
            "Civil Engineering",
            "ARIS"
        ]

        self.program_combo.addItems(programs)

        label6 = QLabel("Program:")
        form_layout.addRow(label6)
        form_layout.addRow(self.program_combo)

        # About
        self.about = QTextEdit()
        self.about.setMaximumHeight(100)

        label7 = QLabel("Tell us a little bit about yourself:")
        form_layout.addRow(label7)
        form_layout.addRow(self.about)

        main_layout.addLayout(form_layout)

        main_layout.addSpacing(15)

        # Checkbox
        self.terms = QCheckBox(
            "I accept the terms and conditions."
        )
        main_layout.addWidget(self.terms)

        main_layout.addSpacing(10)

        # Submit button 
        self.submit_btn = QPushButton("Submit Registration")
        self.submit_btn.setFixedWidth(160)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.submit_btn)
        btn_layout.addStretch()

        main_layout.addLayout(btn_layout)

        main_layout.addStretch()

        self.setLayout(main_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("P2: Student Registration")
        self.setCentralWidget(StudentRegistration())
        self.resize(400, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())