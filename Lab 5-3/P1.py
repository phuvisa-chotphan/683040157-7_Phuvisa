"""
Phuvisa Chotphan
683040157-7
P1
"""
import sys
import os
from PySide6.QtWidgets import (QMessageBox, QGridLayout, QApplication, QMainWindow, QWidget, QLabel, QPushButton, QComboBox, QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class InventoryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("P1: Student scores and grades")
        self.setGeometry(100, 100, 800, 600)

        # store students {id: name}
        self.students = {}

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Input section
        input_layout = QGridLayout()

        # Student ID
        student_label = QLabel("Student ID: ")
        self.student = QComboBox()
        self.student.setPlaceholderText("Select Student ID")

        # load students.txt safely
        file_path = os.path.join(os.path.dirname(__file__), "students.txt")
        try:
            with open(file_path, "r", encoding="utf-8") as f: # encoding="utf-8 --> expect non-english characters
                for line in f:
                    sid, name = line.strip().split(",")
                    self.students[sid] = name
                    self.student.addItem(sid)
        except FileNotFoundError:
            print("students.txt not found")

        input_layout.addWidget(student_label, 0, 0)
        input_layout.addWidget(self.student, 0, 1)

        # Student Name label
        self.name_label = QLabel("")
        input_layout.addWidget(QLabel("Name:"), 0, 2)
        input_layout.addWidget(self.name_label, 0, 3, 1, 3)

        # update name when ID changes
        self.student.currentTextChanged.connect(self.update_name)
        self.update_name()

        # Math
        math_label = QLabel("Math: ")
        input_layout.addWidget(math_label, 1, 0)

        self.math = QSpinBox()
        self.math.setRange(0, 100)
        input_layout.addWidget(self.math, 1, 1)

        # Science
        sci_label = QLabel("Science: ")
        input_layout.addWidget(sci_label, 1, 2)

        self.sci = QSpinBox()
        self.sci.setRange(0, 100)
        input_layout.addWidget(self.sci, 1, 3)

        # English
        eng_label = QLabel("English: ")
        input_layout.addWidget(eng_label, 1, 4)

        self.eng = QSpinBox()
        self.eng.setRange(0, 100)
        input_layout.addWidget(self.eng, 1, 5)

        # Add Student button
        button_layout = QHBoxLayout()

        self.add_button = QPushButton("Add Student")
        self.add_button.clicked.connect(self.add_student)
        button_layout.addWidget(self.add_button)

        # Reset Input button
        self.reset_button = QPushButton("Reset Input")
        self.reset_button.clicked.connect(self.reset_input)
        button_layout.addWidget(self.reset_button)

        # Clear All button
        self.clear_button = QPushButton("Clear Table")
        self.clear_button.clicked.connect(self.clear_all)
        button_layout.addWidget(self.clear_button)

        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)

        # Change button color
        self.add_button.setStyleSheet("background-color: #4886BD; color: white;")
        self.reset_button.setStyleSheet("background-color: #4886BD; color: white;")
        self.clear_button.setStyleSheet("background-color: #4886BD; color: white;")

        # Table 
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["Student ID", "Name", "Math", "Science", "English", "Total", "Average", "Grade"])

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setColumnWidth(0, 100) # stu id col
        self.table.setColumnWidth(1, 200) # stu name col
        self.table.setColumnWidth(2, 75) # math col
        self.table.setColumnWidth(3, 75) # sci col
        self.table.setColumnWidth(4, 75) # eng col
        self.table.setColumnWidth(5, 75) # total col
        self.table.setColumnWidth(6, 75) # average col
        self.table.setColumnWidth(7, 100) # grade col

        main_layout.addWidget(self.table)

    # Update Name
    def update_name(self):
        sid = self.student.currentText()
        self.name_label.setText(self.students.get(sid, ""))
        self.name_label.setStyleSheet("color: #000000; background-color: #D4C69D;")

    # Add Student
    def add_student(self):

        sid = self.student.currentText()
        name = self.students.get(sid, "")

        # validation
        if not sid:
            QMessageBox.warning(self, "Input Error", "Please select the student ID.")
            return

        math = self.math.value()
        sci = self.sci.value()
        eng = self.eng.value()

        if math < 60:
            math_item = QTableWidgetItem((str(math)))
            math_item.setBackground(QColor("#7B1818"))
        else:
            math_item = QTableWidgetItem((str(math)))

        if sci < 60:
            sci_item = QTableWidgetItem((str(sci)))
            sci_item.setBackground(QColor("#7B1818"))
        else:
            sci_item = QTableWidgetItem((str(sci)))

        if eng < 60:
            eng_item = QTableWidgetItem((str(eng)))
            eng_item.setBackground(QColor("#7B1818"))
        else:
            eng_item = QTableWidgetItem((str(eng)))

        total = math + sci + eng
        avg = total / 3

        # grade calculation
        if avg >= 80:
            grade_item = QTableWidgetItem("A")
            grade_item.setBackground(QColor("#2C8B1B"))
        elif avg >= 70:
            grade_item = QTableWidgetItem("B")
        elif avg >= 60:
            grade_item = QTableWidgetItem("C")
        elif avg >= 50:
            grade_item = QTableWidgetItem("D")
        else:
            grade_item = QTableWidgetItem("F")
            grade_item.setBackground(QColor("#7B1818"))

        # 🔴 STOP sorting while inserting
        self.table.setSortingEnabled(False)

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        self.table.setItem(row_position, 0, QTableWidgetItem(sid))
        self.table.setItem(row_position, 1, QTableWidgetItem(name))
        self.table.setItem(row_position, 2, math_item)
        self.table.setItem(row_position, 3, sci_item)
        self.table.setItem(row_position, 4, eng_item)
        self.table.setItem(row_position, 5, QTableWidgetItem(str(total)))
        self.table.setItem(row_position, 6, QTableWidgetItem(f"{avg:.2f}"))
        self.table.setItem(row_position, 7, grade_item)

        # start sorting again
        self.table.setSortingEnabled(True)
        self.table.sortItems(0, Qt.AscendingOrder)

        # reset scores only
        self.math.setValue(0)
        self.sci.setValue(0)
        self.eng.setValue(0)

    # Reset Input
    def reset_input(self):
        """Reset all input fields"""

        self.student.setCurrentIndex(-1)   # back to first student ID
        self.math.setValue(0)
        self.sci.setValue(0)
        self.eng.setValue(0)


    # Clear Table
    def clear_all(self):
        """Clear all table fields"""

        self.table.setRowCount(0)


def main():
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
