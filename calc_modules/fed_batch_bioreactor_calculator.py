from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QGroupBox, QLineEdit, QPushButton, QTextEdit, QFormLayout)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QDoubleValidator

class FedBatchBioreactorCalculator(QWidget):
    """Calculator for fed-batch bioreactor calculations"""

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

        # Substrate Feeding Rate Section
        feeding_rate_group = QGroupBox("Substrate Feeding Rate")
        feeding_rate_layout = QFormLayout()

        self.sf_input = QLineEdit()
        self.sf_input.setValidator(QDoubleValidator(0, 10000, 2))
        feeding_rate_layout.addRow("Substrate Concentration in Feed (Sf):", self.sf_input)

        self.s_input = QLineEdit()
        self.s_input.setValidator(QDoubleValidator(0, 10000, 2))
        feeding_rate_layout.addRow("Substrate Concentration in Reactor (S):", self.s_input)

        self.time_input = QLineEdit()
        self.time_input.setValidator(QDoubleValidator(0, 10000, 2))
        feeding_rate_layout.addRow("Time (t):", self.time_input)

        self.calculate_feeding_rate_button = QPushButton("Calculate Feeding Rate")
        self.calculate_feeding_rate_button.clicked.connect(self.calculate_feeding_rate)
        feeding_rate_layout.addRow(self.calculate_feeding_rate_button)

        feeding_rate_group.setLayout(feeding_rate_layout)
        layout.addWidget(feeding_rate_group)

        # Biomass Concentration Section
        biomass_group = QGroupBox("Biomass Concentration")
        biomass_layout = QFormLayout()

        self.x0_input = QLineEdit()
        self.x0_input.setValidator(QDoubleValidator(0, 10000, 2))
        biomass_layout.addRow("Initial Biomass Concentration (X0):", self.x0_input)

        self.mu_input = QLineEdit()
        self.mu_input.setValidator(QDoubleValidator(0, 100, 4))
        biomass_layout.addRow("Specific Growth Rate (μ):", self.mu_input)

        self.xt_time_input = QLineEdit()
        self.xt_time_input.setValidator(QDoubleValidator(0, 10000, 2))
        biomass_layout.addRow("Time (t):", self.xt_time_input)

        self.calculate_biomass_button = QPushButton("Calculate Biomass Concentration")
        self.calculate_biomass_button.clicked.connect(self.calculate_biomass_concentration)
        biomass_layout.addRow(self.calculate_biomass_button)

        biomass_group.setLayout(biomass_layout)
        layout.addWidget(biomass_group)

        # Product Formation Rate Section
        product_rate_group = QGroupBox("Product Formation Rate")
        product_rate_layout = QFormLayout()

        self.dp_input = QLineEdit()
        self.dp_input.setValidator(QDoubleValidator(0, 10000, 2))
        product_rate_layout.addRow("Change in Product Concentration (dP):", self.dp_input)

        self.dt_input = QLineEdit()
        self.dt_input.setValidator(QDoubleValidator(0, 10000, 2))
        product_rate_layout.addRow("Change in Time (dt):", self.dt_input)

        self.calculate_product_rate_button = QPushButton("Calculate Product Formation Rate")
        self.calculate_product_rate_button.clicked.connect(self.calculate_product_formation_rate)
        product_rate_layout.addRow(self.calculate_product_rate_button)

        product_rate_group.setLayout(product_rate_layout)
        layout.addWidget(product_rate_group)

        # Yield Coefficient Section
        yield_group = QGroupBox("Yield Coefficient")
        yield_layout = QFormLayout()

        self.delta_x_input = QLineEdit()
        self.delta_x_input.setValidator(QDoubleValidator(0, 10000, 2))
        yield_layout.addRow("Change in Biomass Concentration (ΔX):", self.delta_x_input)

        self.delta_s_input = QLineEdit()
        self.delta_s_input.setValidator(QDoubleValidator(0, 10000, 2))
        yield_layout.addRow("Change in Substrate Concentration (ΔS):", self.delta_s_input)

        self.calculate_yield_button = QPushButton("Calculate Yield Coefficient")
        self.calculate_yield_button.clicked.connect(self.calculate_yield_coefficient)
        yield_layout.addRow(self.calculate_yield_button)

        yield_group.setLayout(yield_layout)
        layout.addWidget(yield_group)

        # Results Section
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        layout.addWidget(self.results_text)

    @pyqtSlot()
    def calculate_feeding_rate(self):
        try:
            sf = float(self.sf_input.text())
            s = float(self.s_input.text())
            t = float(self.time_input.text())

            if t <= 0:
                self.results_text.setPlainText("Error: Time must be greater than zero.")
                return

            feeding_rate = (sf - s) / t
            self.results_text.setPlainText(f"Substrate Feeding Rate (Fs): {feeding_rate:.4f}")
        except Exception as e:
            self.results_text.setPlainText(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_biomass_concentration(self):
        try:
            x0 = float(self.x0_input.text())
            mu = float(self.mu_input.text())
            t = float(self.xt_time_input.text())

            biomass_concentration = x0 + (mu * x0 * t)
            self.results_text.setPlainText(f"Biomass Concentration (Xt): {biomass_concentration:.4f}")
        except Exception as e:
            self.results_text.setPlainText(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_product_formation_rate(self):
        try:
            dp = float(self.dp_input.text())
            dt = float(self.dt_input.text())

            if dt <= 0:
                self.results_text.setPlainText("Error: Change in time (dt) must be greater than zero.")
                return

            product_rate = dp / dt
            self.results_text.setPlainText(f"Product Formation Rate (rp): {product_rate:.4f}")
        except Exception as e:
            self.results_text.setPlainText(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_yield_coefficient(self):
        try:
            delta_x = float(self.delta_x_input.text())
            delta_s = float(self.delta_s_input.text())

            if delta_s == 0:
                self.results_text.setPlainText("Error: Change in substrate concentration (ΔS) must not be zero.")
                return

            yield_coefficient = delta_x / delta_s
            self.results_text.setPlainText(f"Yield Coefficient (YX/S): {yield_coefficient:.4f}")
        except Exception as e:
            self.results_text.setPlainText(f"Error: {str(e)}")