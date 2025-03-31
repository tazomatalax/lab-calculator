"""
C1V1 = C2V2 Calculator module
"""
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QFormLayout)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QDoubleValidator

class C1V1Calculator(QWidget):
    """
    Calculator for C1V1 = C2V2 calculations
    """

    def __init__(self):
        """Initialize the C1V1 calculator tab"""
        super().__init__()
        self.create_widgets()
        self.apply_styles()

    def create_widgets(self):
        """Create all the form widgets"""
        main_layout = QVBoxLayout(self)

        # Create input group
        input_group = QGroupBox("C1V1 = C2V2 Calculator")
        input_layout = QFormLayout(input_group)

        # C1 input
        self.c1_input = QLineEdit()
        self.c1_input.setValidator(QDoubleValidator(0, 10000, 4))
        input_layout.addRow("Concentration 1 (C1):", self.c1_input)

        # V1 input
        self.v1_input = QLineEdit()
        self.v1_input.setValidator(QDoubleValidator(0, 10000, 4))
        input_layout.addRow("Volume 1 (V1):", self.v1_input)

        # C2 input
        self.c2_input = QLineEdit()
        self.c2_input.setValidator(QDoubleValidator(0, 10000, 4))
        input_layout.addRow("Concentration 2 (C2):", self.c2_input)

        # V2 input
        self.v2_input = QLineEdit()
        self.v2_input.setValidator(QDoubleValidator(0, 10000, 4))
        input_layout.addRow("Volume 2 (V2):", self.v2_input)

        # Calculate button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_c1v1)
        input_layout.addRow(self.calculate_button)

        main_layout.addWidget(input_group)

    def apply_styles(self):
        """Apply styles to the widget"""
        self.setStyleSheet(
            """
            QWidget {
                font-family: Arial, sans-serif;
                font-size: 14px;
            }

            QGroupBox {
                border: 2px solid #4CAF50;
                border-radius: 5px;
                margin-top: 10px;
                padding: 10px;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 3px;
                color: #4CAF50;
                font-weight: bold;
            }

            QLabel {
                color: #333;
            }

            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                background: #f9f9f9;
            }

            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #45a049;
            }

            QPushButton:pressed {
                background-color: #3e8e41;
            }
            """
        )

    @pyqtSlot()
    def calculate_c1v1(self):
        """Calculate the missing value in C1V1 = C2V2"""
        try:
            c1 = self.c1_input.text()
            v1 = self.v1_input.text()
            c2 = self.c2_input.text()
            v2 = self.v2_input.text()

            # Convert inputs to floats or None if empty
            c1 = float(c1) if c1 else None
            v1 = float(v1) if v1 else None
            c2 = float(c2) if c2 else None
            v2 = float(v2) if v2 else None

            # Calculate the missing value
            if c1 is None and v1 and c2 and v2:
                c1 = (c2 * v2) / v1
                self.c1_input.setText(f"{c1:.4f}")
            elif v1 is None and c1 and c2 and v2:
                v1 = (c2 * v2) / c1
                self.v1_input.setText(f"{v1:.4f}")
            elif c2 is None and c1 and v1 and v2:
                c2 = (c1 * v1) / v2
                self.c2_input.setText(f"{c2:.4f}")
            elif v2 is None and c1 and v1 and c2:
                v2 = (c1 * v1) / c2
                self.v2_input.setText(f"{v2:.4f}")
            else:
                raise ValueError("Please provide exactly three values.")
        except Exception as e:
            self.c1_input.setText("Error")
            self.v1_input.setText("Error")
            self.c2_input.setText("Error")
            self.v2_input.setText("Error")