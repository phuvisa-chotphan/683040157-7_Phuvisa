"""
Phuvisa Chotphan
683040157-7
P1
"""
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QLabel, QLineEdit)
from PySide6.QtWidgets import QPushButton, QComboBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

kg = "kilograms"
lb = "pounds"
cm = "centimeters"
m = "meters"
ft = "feet"
adult = "Adults 20+"
child = "Children and Teenagers (5-19)"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("P1: BMI Calculator")
        self.setGeometry(100, 100, 400, 650) 

        # widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)

        
        self.input_section = InputSection()
        main_layout.addWidget(self.input_section)
        
        self.output_section = OutputSection()

        result_container = QWidget()
        result_container.setStyleSheet("background-color: #FAF0E6; border-radius: 10px;")  # Linen color
        
        container_layout = QVBoxLayout(result_container)
        container_layout.addWidget(self.output_section)
        
        main_layout.addWidget(result_container)
        main_layout.addStretch()

        # connect signals 
        self.input_section.btn_submit.clicked.connect(lambda: self.input_section.submit_reg(self.output_section))
        self.input_section.btn_clear.clicked.connect(lambda: self.input_section.clear_form(self.output_section))


class OutputSection(QWidget):
    def __init__(self):
        super().__init__()
        
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.setSpacing(10)

        lbl_title = QLabel("Your BMI")
        lbl_title.setAlignment(Qt.AlignCenter)
        lbl_title.setFont(QFont("Arial", 12))
        self.main_layout.addWidget(lbl_title)

        self.lbl_value = QLabel("0.00")
        self.lbl_value.setAlignment(Qt.AlignCenter)
        self.lbl_value.setFont(QFont("Arial", 30, QFont.Bold))
        self.lbl_value.setStyleSheet("color: #4444FF;")
        self.main_layout.addWidget(self.lbl_value)

        self.main_layout.addSpacing(10)


    def show_adult_table(self, bmi_value):
        table_layout = QGridLayout()
        
        # Header
        label = QLabel("BMI")
        label.setFont(QFont("Arial", 10, QFont.Bold))
        table_layout.addWidget(label, 0, 0, alignment=Qt.AlignCenter)
        
        label = QLabel("Condition")
        label.setFont(QFont("Arial", 10, QFont.Bold))
        table_layout.addWidget(label, 0, 1, alignment=Qt.AlignCenter)
        data = [
            ("< 18.5", "Thin", "#FAF0E6"),
            ("18.5 - 25.0", "Normal", "#FAF0E6"),
            ("25.1 - 30.0", "Overweight", "#FAF0E6"),
            ("> 30.0", "Obese", "#FAF0E6")
        ]

        for i, (rng, cond, color) in enumerate(data):
            row = i + 1
            
            lbl_rng = QLabel(rng)
            lbl_rng.setAlignment(Qt.AlignCenter)
            lbl_cond = QLabel(cond)
            lbl_cond.setAlignment(Qt.AlignCenter)
            style = f"background-color: {color}; padding: 5px;"
            font = QFont("Arial", 10)
            lbl_rng.setStyleSheet(style)
            lbl_cond.setStyleSheet(style)
            lbl_rng.setFont(font)
            lbl_cond.setFont(font)

            table_layout.addWidget(lbl_rng, row, 0)
            table_layout.addWidget(lbl_cond, row, 1)

        self.main_layout.addLayout(table_layout)

    def show_child_link(self):
        
        info_label = QLabel("For child's BMI interpretation, please click one of the following links.")
        info_label.setWordWrap(True)
        info_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(info_label)

        link_layout = QHBoxLayout()
        boy_link = QLabel('<a href="https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/bmi-for-age-(5-19-years)/cht-bmifa-boys-z-5-19years.pdf?sfvrsn=4007e921_4">BMI graph for BOYS</a>')
        girl_link = QLabel('<a href="https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/bmi-for-age-(5-19-years)/cht-bmifa-girls-z-5-19years.pdf?sfvrsn=c708a56b_4">BMI graph for GIRLS</a>')
        
        boy_link.setOpenExternalLinks(True)
        girl_link.setOpenExternalLinks(True)
        
        link_layout.addWidget(boy_link)
        boy_link.setAlignment(Qt.AlignCenter)
        link_layout.addWidget(girl_link)
        
        self.main_layout.addLayout(link_layout)

    def update_results(self, bmi, age_group):
        self.clear_result()
        self.lbl_value.setText(f"{bmi:.2f}")

        if age_group == adult:
            self.show_adult_table(bmi)
        else:
            self.show_child_link()
    
    def clear_result(self):
        layout = self.layout()
        if layout is None: return

        while layout.count() > 3:
            item = layout.takeAt(3)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())
    
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())

class InputSection(QWidget):

    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.setSpacing(10)

        header = QLabel("Adult and Child BMI Calculator")
        header.setAlignment(Qt.AlignCenter)
        header.setFont(QFont("Arial", 14, QFont.Bold))
        header.setStyleSheet("background-color: #A93226; color: white; padding: 10px; border-radius: 5px;")
        self.main_layout.addWidget(header)

        # Form Inputs
        form_layout = QGridLayout()
        
        # Age
        form_layout.addWidget(QLabel("BMI age group:"), 0, 0, alignment=Qt.AlignRight)
        self.combo_age = QComboBox()
        self.combo_age.addItems([adult, child])
        form_layout.addWidget(self.combo_age, 0, 1)

        # Weight
        form_layout.addWidget(QLabel("Weight:"), 1, 0, alignment=Qt.AlignRight)
        w_box = QHBoxLayout()
        self.txt_weight = QLineEdit()
        self.combo_w_unit = QComboBox()
        self.combo_w_unit.addItems([kg, lb])
        w_box.addWidget(self.txt_weight)
        w_box.addWidget(self.combo_w_unit)
        form_layout.addLayout(w_box, 1, 1)

        # Height
        form_layout.addWidget(QLabel("Height:"), 2, 0, alignment=Qt.AlignRight)
        h_box = QHBoxLayout()
        self.txt_height = QLineEdit()
        self.combo_h_unit = QComboBox()
        self.combo_h_unit.addItems([cm, m, ft])
        h_box.addWidget(self.txt_height)
        h_box.addWidget(self.combo_h_unit)
        form_layout.addLayout(h_box, 2, 1)

        self.main_layout.addLayout(form_layout)

        # Buttons
        btn_layout = QHBoxLayout()
        self.btn_clear = QPushButton("clear")
        self.btn_submit = QPushButton("Submit Registration")
        
        btn_layout.addWidget(self.btn_clear)
        btn_layout.addWidget(self.btn_submit)
        
        self.main_layout.addLayout(btn_layout)

    def clear_form(self, output_section):
        # clear input
        self.txt_weight.clear()
        self.txt_height.clear()
        self.combo_age.setCurrentIndex(0)
        self.combo_w_unit.setCurrentIndex(0)
        self.combo_h_unit.setCurrentIndex(0)

        # clear output 
        output_section.lbl_value.setText("0.00")
        output_section.clear_result()

    def submit_reg(self, output_section):
        bmi = self.calculate_BMI()
        if bmi is not None:
            age_group = self.combo_age.currentText()
            output_section.update_results(bmi, age_group)
        else:
            output_section.lbl_value.setText("Error")

    def calculate_BMI(self):
        try:
            w_text = self.txt_weight.text()
            h_text = self.txt_height.text()

            if not w_text or not h_text:
                return None

            w = float(w_text)
            h = float(h_text)
            
            w_unit = self.combo_w_unit.currentText()
            h_unit = self.combo_h_unit.currentText()

            # (kg, m)
            if w_unit == lb:
                w = w * 0.453592
            
            if h_unit == cm:
                h = h / 100
            elif h_unit == ft:
                h = h * 0.3048
            if h == 0: return None
            return w / (h ** 2)

        except ValueError:
            return None

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()