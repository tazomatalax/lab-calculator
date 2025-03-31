from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, 
                            QLabel, QLineEdit, QPushButton, QTextEdit, QFormLayout, QTabWidget)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QDoubleValidator

class ContinuousBioreactorCalculator(QWidget):
    """Calculator for continuous bioreactor calculations"""

    def __init__(self):
        super().__init__()
        self.create_widgets()
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

    def create_widgets(self):
        layout = QVBoxLayout(self)

        # Dilution Rate Section
        dilution_rate_group = QGroupBox("Dilution Rate Calculation")
        dilution_rate_layout = QFormLayout()

        self.flow_rate_input = QLineEdit()
        self.flow_rate_input.setValidator(QDoubleValidator(0, 10000, 2))
        dilution_rate_layout.addRow("Flow Rate (F):", self.flow_rate_input)

        self.volume_input = QLineEdit()
        self.volume_input.setValidator(QDoubleValidator(0, 10000, 2))
        dilution_rate_layout.addRow("Volume (V):", self.volume_input)

        self.calculate_dilution_rate_button = QPushButton("Calculate Dilution Rate")
        self.calculate_dilution_rate_button.clicked.connect(self.calculate_dilution_rate)
        dilution_rate_layout.addRow(self.calculate_dilution_rate_button)

        dilution_rate_group.setLayout(dilution_rate_layout)
        layout.addWidget(dilution_rate_group)

        # Steady-State Biomass Concentration Section
        biomass_group = QGroupBox("Steady-State Biomass Concentration")
        biomass_layout = QFormLayout()

        self.mu_max_input = QLineEdit()
        self.mu_max_input.setValidator(QDoubleValidator(0, 100, 4))
        biomass_layout.addRow("Maximum Specific Growth Rate (μmax):", self.mu_max_input)

        self.ss_substrate_input = QLineEdit()
        self.ss_substrate_input.setValidator(QDoubleValidator(0, 10000, 2))
        biomass_layout.addRow("Steady-State Substrate Concentration (Sss):", self.ss_substrate_input)

        self.ks_input = QLineEdit()
        self.ks_input.setValidator(QDoubleValidator(0, 10000, 2))
        biomass_layout.addRow("Half-Saturation Constant (Ks):", self.ks_input)

        self.calculate_biomass_button = QPushButton("Calculate Biomass Concentration")
        self.calculate_biomass_button.clicked.connect(self.calculate_biomass_concentration)
        biomass_layout.addRow(self.calculate_biomass_button)

        biomass_group.setLayout(biomass_layout)
        layout.addWidget(biomass_group)

        # Substrate Utilization Rate Section
        substrate_group = QGroupBox("Substrate Utilization Rate")
        substrate_layout = QFormLayout()

        self.sin_input = QLineEdit()
        self.sin_input.setValidator(QDoubleValidator(0, 10000, 2))
        substrate_layout.addRow("Substrate Concentration in Feed (Sin):", self.sin_input)

        self.ss_substrate_util_input = QLineEdit()
        self.ss_substrate_util_input.setValidator(QDoubleValidator(0, 10000, 2))
        substrate_layout.addRow("Steady-State Substrate Concentration (Sss):", self.ss_substrate_util_input)

        self.ss_biomass_input = QLineEdit()
        self.ss_biomass_input.setValidator(QDoubleValidator(0, 10000, 2))
        substrate_layout.addRow("Steady-State Biomass Concentration (Xss):", self.ss_biomass_input)

        self.calculate_substrate_button = QPushButton("Calculate Substrate Utilization Rate")
        self.calculate_substrate_button.clicked.connect(self.calculate_substrate_utilization_rate)
        substrate_layout.addRow(self.calculate_substrate_button)

        substrate_group.setLayout(substrate_layout)
        layout.addWidget(substrate_group)

        # Productivity Section
        productivity_group = QGroupBox("Productivity")
        productivity_layout = QFormLayout()

        self.ss_product_input = QLineEdit()
        self.ss_product_input.setValidator(QDoubleValidator(0, 10000, 2))
        productivity_layout.addRow("Steady-State Product Concentration (Pss):", self.ss_product_input)

        self.calculate_productivity_button = QPushButton("Calculate Productivity")
        self.calculate_productivity_button.clicked.connect(self.calculate_productivity)
        productivity_layout.addRow(self.calculate_productivity_button)

        productivity_group.setLayout(productivity_layout)
        layout.addWidget(productivity_group)

        # Results Section
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        layout.addWidget(self.results_text)

    @pyqtSlot()
    def calculate_dilution_rate(self):
        try:
            flow_rate = float(self.flow_rate_input.text())
            volume = float(self.volume_input.text())

            if volume <= 0:
                self.results_text.setPlainText("Error: Volume must be greater than zero.")
                return

            dilution_rate = flow_rate / volume
            self.results_text.setPlainText(f"Dilution Rate (D): {dilution_rate:.4f}")
        except Exception as e:
            self.results_text.setPlainText(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_biomass_concentration(self):
        try:
            mu_max = float(self.mu_max_input.text())
            ss_substrate = float(self.ss_substrate_input.text())
            ks = float(self.ks_input.text())

            biomass_concentration = (mu_max * ss_substrate) / (ks + ss_substrate)
            self.results_text.setPlainText(f"Steady-State Biomass Concentration (Xss): {biomass_concentration:.4f}")
        except Exception as e:
            self.results_text.setPlainText(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_substrate_utilization_rate(self):
        try:
            dilution_rate = float(self.flow_rate_input.text()) / float(self.volume_input.text())
            sin = float(self.sin_input.text())
            ss_substrate = float(self.ss_substrate_util_input.text())
            ss_biomass = float(self.ss_biomass_input.text())

            substrate_utilization_rate = dilution_rate * (sin - ss_substrate) * ss_biomass
            self.results_text.setPlainText(f"Substrate Utilization Rate (rs): {substrate_utilization_rate:.4f}")
        except Exception as e:
            self.results_text.setPlainText(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_productivity(self):
        try:
            dilution_rate = float(self.flow_rate_input.text()) / float(self.volume_input.text())
            ss_product = float(self.ss_product_input.text())

            productivity = dilution_rate * ss_product
            self.results_text.setPlainText(f"Productivity (P): {productivity:.4f}")
        except Exception as e:
            self.results_text.setPlainText(f"Error: {str(e)}")