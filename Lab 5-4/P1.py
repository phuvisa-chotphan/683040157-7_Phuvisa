"""
Phuvisa Chotphan
683040157-7
P1
"""
import sys
import pyperclip
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QGridLayout, QLineEdit, QLabel, QWidget, QVBoxLayout, QSpinBox, QComboBox, QPushButton, QHBoxLayout, QColorDialog, QFileDialog, QFrame, QStyle
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QLocale, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: Personal Info Card")
        self.resize(400, 450)

        self.setStyleSheet("""
            QWidget {
                background-color: white;
                color: black;
            }
        """)

        self.current_color = None

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Create menu bar
        self.menu_bar = self.menuBar()

        # Create File menu
        file_menu = self.menu_bar.addMenu("&File")

        # Add actions to File menu
        gene_action = QAction("&Generate Card", self)
        gene_action.triggered.connect(self.generate_card)
        file_menu.addAction(gene_action)

        save_action = QAction("&Save Card", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        cleardisplay_action = QAction("&Clear Display", self)
        cleardisplay_action.triggered.connect(self.clear_display)
        file_menu.addAction(cleardisplay_action)

        # Add Exit action
        exit_action = QAction("E&xit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create Edit menu
        edit_menu = self.menu_bar.addMenu("&Edit")

        # Add actions to Edit menu
        copy_action = QAction("&Copy Card", self)
        copy_action.triggered.connect(self.copy)
        edit_menu.addAction(copy_action)

        clearform_action = QAction("&Clear Form", self)
        clearform_action.triggered.connect(self.clear_form)
        edit_menu.addAction(clearform_action)

        # Toolbar
        toolbar = self.addToolBar("Main Toolbar")

        style = self.style()

        gene_action = QAction(style.standardIcon(QStyle.SP_MediaPlay), "Generate", self)
        toolbar.addAction(gene_action)
        save_action = QAction(style.standardIcon(QStyle.SP_DialogSaveButton), "Save", self)
        toolbar.addAction(save_action)
        clear_action = QAction(style.standardIcon(QStyle.SP_TrashIcon), "Clear", self)
        toolbar.addAction(clear_action)

        gene_action.triggered.connect(self.generate_card)
        save_action.triggered.connect(self.save_file)
        clear_action.triggered.connect(self.clear_form)
        clear_action.triggered.connect(self.clear_display)

        # FormLayout 
        input_layout = QGridLayout()
        input_layout.setVerticalSpacing(10)

        # Full Name
        self.name_input = QLineEdit()
        self.name_input.setMaximumWidth(300)
        self.name_input.setPlaceholderText("First name and Lastname")
        label1 = QLabel("Fullname:")
        input_layout.addWidget(label1, 0, 0)
        input_layout.addWidget(self.name_input, 0, 1)
       
        # Age
        age_label = QLabel("Age: ")
        input_layout.addWidget(age_label, 1, 0)

        self.age = QSpinBox()
        self.age.setRange(1,120)
        self.age.setValue(25)
        self.age.setLocale(QLocale(QLocale.English))
        input_layout.addWidget(self.age, 1, 1)

        # Email
        self.email_input = QLineEdit()
        self.email_input.setMaximumWidth(300)
        self.email_input.setPlaceholderText("username@domain.name")
        label2 = QLabel("Email:")
        input_layout.addWidget(label2, 2, 0)
        input_layout.addWidget(self.email_input, 2, 1)

        # Position
        self.position_combo = QComboBox()

        self.position_combo.setPlaceholderText("Choose your position")

        positions = ["Teaching Staff","Supporting Staff","Student","Visitor"]

        self.position_combo.addItems(positions)

        label3 = QLabel("Position:")
        input_layout.addWidget(label3, 3, 0)
        input_layout.addWidget(self.position_combo, 3, 1)

        # Color picker
        self.color_preview = QLabel()
        self.color_preview.setFixedSize(40, 20)
        self.color_preview.setStyleSheet("background: #a8d5e2; border:1px solid black;")

        self.color_btn = QPushButton("Pick New Color")
        self.color_btn.clicked.connect(self.pick_color)

        color_layout = QHBoxLayout()
        color_layout.addWidget(self.color_preview)
        color_layout.addWidget(self.color_btn)

        label4 = QLabel("Your favorite color:")
        input_layout.addWidget(label4, 4, 0)
        input_layout.addLayout(color_layout, 4, 1)

        # Card Display
        self.card_display = QLabel()

        self.card_display.setMinimumHeight(150)
        self.card_display.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.card_display.setWordWrap(True)
        self.generate_card()

        self.card_display.setStyleSheet("""
            QLabel {
                border-radius: 10px;
                padding: 15px;
                background: #a8d5e2;
            }
        """)

        # Display all form and card display
        main_layout.addLayout(input_layout)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)
        main_layout.addWidget(self.card_display)
        main_layout.addStretch()

    def generate_card(self):
        name = self.name_input.text() or "Your name here"
        age = self.age.value()
        email = self.email_input.text() or "your_username@domain.name"

        # if you have position widget
        position_text = self.position_combo.currentText()

        if not position_text:
            position_text = "Your position here"

        bg = self.current_color if self.current_color else "#a8d5e2"

        self.card_display.setStyleSheet(f"""
            QLabel {{
                border-radius: 10px;
                padding: 15px;
                background: {bg};
                }}
            """)

        html = f"""
        <div style="
            background:{bg};
            border-radius:10px;
            padding:15px;
        ">
            <div style="font-size:20px; font-weight:bold; color:#222;">
                {name}
            </div>

            <div style="color:#333;">
                ({age})
            </div>

            <br>

            <div style="font-size:16px; color:#222;">
                {position_text}
            </div>

            <div style="margin-top:8px; color:#222;">
                <table cellpadding="0" cellspacing="0">
                    <tr>
                        <td style="font-size:30px; padding-right:6px;">✉</td>
                        <td style="vertical-align:middle; white-space:nowrap;">{email}</td>
                    </tr>
                </table>
            </div>
        </div>
        """

        self.card_display.setText(html)

        self.current_card_text = f"{name}\n({age})\n{position_text}\nEmail: {email}"

        self.statusBar().showMessage("Card generated")

    def save_file(self):
        if not hasattr(self, "current_card_text"):
            self.statusBar().showMessage("Nothing to save")
            return

        file_name, _ = QFileDialog.getSaveFileName(self, "Save Card", "card.txt", "Text Files (*.txt)")

        if file_name:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(self.current_card_text)

            self.statusBar().showMessage("Card saved")

    def clear_display(self):

        bg = self.current_color if self.current_color else "#a8d5e2"

        placeholder_html = f"""
        <div style="
            background:#a8d5e2;
            border-radius:10px;
            padding:15px;
        ">
        <div style="font-size:20px; font-weight:bold; color:#222;">
            Your name here
        </div>

        <div style="color:#333;">
                (Age)
        </div>

        <br>

        <div style="font-size:16px; color:#222;">
                Your position here
        </div>

            <div style="margin-top:8px; color:#222;">
                <table cellpadding="0" cellspacing="0">
                    <tr>
                        <td style="font-size:30px; padding-right:6px;">✉</td>
                        <td style="vertical-align:middle;">your_username@domain.name</td>
                     </tr>
                </table>
            </div>
        </div>
        """
        self.card_display.setStyleSheet(f"background-color: #a8d5e2; border-radius: 10px; padding: 15px;")
        self.card_display.setText(placeholder_html)
        self.statusBar().showMessage("Display cleared")

    def copy(self):
        if not hasattr(self, "current_card_text"):
            self.statusBar().showMessage("Nothing to copy")
            return

        pyperclip.copy(self.current_card_text)
        self.statusBar().showMessage("Card copied to clipboard")

    def clear_form(self):
        self.name_input.clear()
        self.age.setValue(25)
        self.email_input.clear()
        self.position_combo.setCurrentIndex(-1)

        # ✅ restore default color
        self.current_color = "#a8d5e2"
        self.color_preview.setStyleSheet(f"background-color: {self.current_color}; border:1px solid gray;")

    def pick_color(self):

        color = QColorDialog.getColor()

        if color.isValid():
            self.current_color = color.name()

            self.color_preview.setStyleSheet(f"background:{self.current_color}; border:1px solid black;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())