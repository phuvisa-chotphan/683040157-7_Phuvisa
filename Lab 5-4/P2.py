"""
Phuvisa Chotphan
683040157-7
P2
"""

import sys
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QComboBox,
    QSlider, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout,
    QProgressBar, QFileDialog, QStatusBar, QToolBar
)
from PySide6.QtCore import Qt, QLocale
from PySide6.QtGui import QAction, QIcon


MAX_POINTS = 40


class CharacterBuilder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RPG Character Builder")
        self.setFixedSize(750, 500)

        self.setup_ui()
        self.create_menu()
        self.create_toolbar()
        self.create_statusbar()

    # =========================
    # UI SETUP
    # =========================
    def setup_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QHBoxLayout(main_widget)

        # LEFT PANEL
        left_layout = QVBoxLayout()

        form_layout = QGridLayout()

        # Name
        form_layout.addWidget(QLabel("Character Name:"), 0, 0)
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter character name...")
        form_layout.addWidget(self.name_input, 0, 1)

        # Race
        form_layout.addWidget(QLabel("Race:"), 1, 0)
        self.race_combo = QComboBox()
        self.race_combo.setPlaceholderText("Choose race")
        self.race_combo.addItems(["Human", "Elf", "Dwarf", "Orc", "Undead"])
        form_layout.addWidget(self.race_combo, 1, 1)

        # Class
        form_layout.addWidget(QLabel("Class:"), 2, 0)
        self.class_combo = QComboBox()
        self.class_combo.setPlaceholderText("Choose class")
        self.class_combo.addItems(["Warrior", "Mage", "Rogue", "Paladin", "Ranger"])
        form_layout.addWidget(self.class_combo, 2, 1)

        # Gender
        form_layout.addWidget(QLabel("Gender:"), 3, 0)
        self.gender_combo = QComboBox()
        self.gender_combo.setPlaceholderText("Choose gender")
        self.gender_combo.addItems(["Male", "Female", "Other"])
        form_layout.addWidget(self.gender_combo, 3, 1)

        left_layout.addLayout(form_layout)

        # === STAT SECTION ===
        self.stats = {}
        self.stat_labels = {}

        for stat in ["STR", "DEX", "INT", "VIT"]:
            layout = QHBoxLayout()

            label = QLabel(stat)
            slider = QSlider(Qt.Horizontal)
            slider.setRange(1, 20)
            slider.setValue(5)
            slider.valueChanged.connect(self.update_total)

            value_label = QLabel("5")

            slider.valueChanged.connect(
                lambda value, l=value_label: l.setText(str(value))
            )

            layout.addWidget(label)
            layout.addWidget(slider)
            layout.addWidget(value_label)

            left_layout.addLayout(layout)

            self.stats[stat] = slider
            self.stat_labels[stat] = value_label

        # Total label
        self.total_label = QLabel("Points used: 20 / 40")
        left_layout.addWidget(self.total_label)

        # Generate button
        self.generate_button = QPushButton("Generate Character Sheet")
        self.generate_button.clicked.connect(self.generate_sheet)
        left_layout.addWidget(self.generate_button)

        left_layout.addStretch()

        # RIGHT PANEL (Character Sheet)
        self.sheet_widget = QWidget()
        self.sheet_widget.setFixedWidth(250)
        self.sheet_widget.setStyleSheet("background-color: #1e1e2f; color: white;")

        sheet_layout = QVBoxLayout(self.sheet_widget)

        self.sheet_name = QLabel("— Character Name —")
        self.sheet_name.setAlignment(Qt.AlignCenter)
        sheet_layout.addWidget(self.sheet_name)

        self.sheet_info = QLabel("Race • Class")
        self.sheet_info.setAlignment(Qt.AlignCenter)
        sheet_layout.addWidget(self.sheet_info)

        sheet_layout.addSpacing(20)

        self.progress_bars = {}

        for stat in ["STR", "DEX", "INT", "VIT"]:
            label = QLabel(stat)
            bar = QProgressBar()
            bar.setRange(0, 20)
            bar.setValue(5)

            sheet_layout.addWidget(label)
            sheet_layout.addWidget(bar)

            self.progress_bars[stat] = bar

        sheet_layout.addStretch()

        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.sheet_widget)

    # =========================
    # MENU
    # =========================
    def create_menu(self):
        menubar = self.menuBar()

        game_menu = menubar.addMenu("Game")
        edit_menu = menubar.addMenu("Edit")

        # Game menu actions
        new_action = QAction("New Character", self)
        new_action.triggered.connect(self.reset_all)

        generate_action = QAction("Generate Sheet", self)
        generate_action.triggered.connect(self.generate_sheet)

        save_action = QAction("Save Sheet", self)
        save_action.triggered.connect(self.save_sheet)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        game_menu.addAction(new_action)
        game_menu.addAction(generate_action)
        game_menu.addAction(save_action)
        game_menu.addSeparator()
        game_menu.addAction(exit_action)

        # Edit menu
        reset_stats_action = QAction("Reset Stats", self)
        reset_stats_action.triggered.connect(self.reset_stats)

        random_action = QAction("Randomize", self)
        random_action.triggered.connect(self.randomize_character)

        edit_menu.addAction(reset_stats_action)
        edit_menu.addAction(random_action)

    # =========================
    # TOOLBAR
    # =========================
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        new_action = QAction(QIcon.fromTheme("document-new"), "", self)
        new_action.triggered.connect(self.reset_all)

        generate_action = QAction(QIcon.fromTheme("media-playback-start"), "", self)
        generate_action.triggered.connect(self.generate_sheet)

        random_action = QAction(QIcon.fromTheme("view-refresh"), "", self)
        random_action.triggered.connect(self.randomize_character)

        save_action = QAction(QIcon.fromTheme("document-save"), "", self)
        save_action.triggered.connect(self.save_sheet)

        toolbar.addAction(new_action)
        toolbar.addAction(generate_action)
        toolbar.addAction(random_action)
        toolbar.addAction(save_action)

    # =========================
    # STATUS BAR
    # =========================
    def create_statusbar(self):
        status = QStatusBar()
        self.setStatusBar(status)
        status.showMessage("Ready to create your character")
        status.addPermanentWidget(QLabel("Created by YourName"))

    # =========================
    # FUNCTIONS
    # =========================
    def update_total(self):
        total = sum(slider.value() for slider in self.stats.values())

        self.total_label.setText(f"Points used: {total} / 40")

        if total > MAX_POINTS:
            self.total_label.setStyleSheet("color: red;")
        else:
            self.total_label.setStyleSheet("color: black;")

    def generate_sheet(self):
        name = self.name_input.text() or "Unknown Hero"
        race = self.race_combo.currentText()
        char_class = self.class_combo.currentText()

        self.sheet_name.setText(name)
        self.sheet_info.setText(f"{race} • {char_class}")

        for stat, slider in self.stats.items():
            self.progress_bars[stat].setValue(slider.value())

        self.statusBar().showMessage("Character sheet generated!", 3000)

    def reset_stats(self):
        for slider in self.stats.values():
            slider.setValue(5)
        self.statusBar().showMessage("Stats reset!", 3000)

    def reset_all(self):
        self.name_input.clear()
        self.race_combo.setCurrentIndex(0)
        self.class_combo.setCurrentIndex(0)
        self.gender_combo.setCurrentIndex(0)
        self.reset_stats()
        self.statusBar().showMessage("New character created!", 3000)

    def randomize_character(self):
        self.name_input.setText("RandomHero")

        self.race_combo.setCurrentIndex(random.randint(0, 4))
        self.class_combo.setCurrentIndex(random.randint(0, 4))
        self.gender_combo.setCurrentIndex(random.randint(0, 2))

        remaining = MAX_POINTS
        for stat in self.stats.values():
            value = random.randint(1, min(20, remaining))
            stat.setValue(value)
            remaining -= value
            if remaining <= 0:
                break

        self.update_total()
        self.statusBar().showMessage("Character randomized!", 3000)

    def save_sheet(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Sheet", "", "Text Files (*.txt)")
        if not file_path:
            return

        with open(file_path, "w") as file:
            file.write(f"Name: {self.sheet_name.text()}\n")
            file.write(f"Info: {self.sheet_info.text()}\n\n")
            for stat, slider in self.stats.items():
                file.write(f"{stat}: {slider.value()}\n")

        self.statusBar().showMessage("Character sheet saved!", 3000)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    QLocale.setDefault(QLocale(QLocale.English, QLocale.UnitedStates))

    window = CharacterBuilder()
    window.show()
    sys.exit(app.exec())