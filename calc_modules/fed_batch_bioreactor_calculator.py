from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLineEdit, QPushButton, QTextEdit, QFormLayout)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QDoubleValidator
import datetime

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
        # Create main horizontal layout with inputs on left, results on right
        main_layout = QHBoxLayout(self)
        
        # Create left panel for inputs
        input_group = QGroupBox("Inputs")
        input_layout = QVBoxLayout(input_group)
        
        # Create right panel for results
        results_group = QGroupBox("Results")
        results_layout = QVBoxLayout(results_group)
        
        # Add panels to main layout
        main_layout.addWidget(input_group)
        main_layout.addWidget(results_group)

        # Substrate Feeding Rate Section
        feeding_rate_group = QGroupBox("Substrate Feeding Rate")
        feeding_rate_layout = QFormLayout()

        self.sf_input = QLineEdit()
        self.sf_input.setValidator(QDoubleValidator(0, 10000, 2))
        feeding_rate_layout.addRow("Substrate Concentration in Feed (Sf) [g/L]:", self.sf_input)

        self.s_input = QLineEdit()
        self.s_input.setValidator(QDoubleValidator(0, 10000, 2))
        feeding_rate_layout.addRow("Substrate Concentration in Reactor (S) [g/L]:", self.s_input)

        self.time_input = QLineEdit()
        self.time_input.setValidator(QDoubleValidator(0, 10000, 2))
        feeding_rate_layout.addRow("Time (t) [h]:", self.time_input)

        self.calculate_feeding_rate_button = QPushButton("Calculate Feeding Rate")
        self.calculate_feeding_rate_button.clicked.connect(self.calculate_feeding_rate)
        feeding_rate_layout.addRow(self.calculate_feeding_rate_button)

        feeding_rate_group.setLayout(feeding_rate_layout)
        input_layout.addWidget(feeding_rate_group)

        # Biomass Concentration Section
        biomass_group = QGroupBox("Biomass Concentration")
        biomass_layout = QFormLayout()

        self.x0_input = QLineEdit()
        self.x0_input.setValidator(QDoubleValidator(0, 10000, 2))
        biomass_layout.addRow("Initial Biomass Concentration (X0) [g/L]:", self.x0_input)

        self.mu_input = QLineEdit()
        self.mu_input.setValidator(QDoubleValidator(0, 100, 4))
        biomass_layout.addRow("Specific Growth Rate (μ) [h⁻¹]:", self.mu_input)

        self.xt_time_input = QLineEdit()
        self.xt_time_input.setValidator(QDoubleValidator(0, 10000, 2))
        biomass_layout.addRow("Time (t) [h]:", self.xt_time_input)

        self.calculate_biomass_button = QPushButton("Calculate Biomass Concentration")
        self.calculate_biomass_button.clicked.connect(self.calculate_biomass_concentration)
        biomass_layout.addRow(self.calculate_biomass_button)

        biomass_group.setLayout(biomass_layout)
        input_layout.addWidget(biomass_group)

        # Product Formation Rate Section
        product_rate_group = QGroupBox("Product Formation Rate")
        product_rate_layout = QFormLayout()

        self.dp_input = QLineEdit()
        self.dp_input.setValidator(QDoubleValidator(0, 10000, 2))
        product_rate_layout.addRow("Change in Product Concentration (dP) [g/L]:", self.dp_input)

        self.dt_input = QLineEdit()
        self.dt_input.setValidator(QDoubleValidator(0, 10000, 2))
        product_rate_layout.addRow("Change in Time (dt) [h]:", self.dt_input)

        self.calculate_product_rate_button = QPushButton("Calculate Product Formation Rate")
        self.calculate_product_rate_button.clicked.connect(self.calculate_product_formation_rate)
        product_rate_layout.addRow(self.calculate_product_rate_button)

        product_rate_group.setLayout(product_rate_layout)
        input_layout.addWidget(product_rate_group)

        # Yield Coefficient Section
        yield_group = QGroupBox("Yield Coefficient")
        yield_layout = QFormLayout()

        self.delta_x_input = QLineEdit()
        self.delta_x_input.setValidator(QDoubleValidator(0, 10000, 2))
        yield_layout.addRow("Change in Biomass Concentration (ΔX) [g/L]:", self.delta_x_input)

        self.delta_s_input = QLineEdit()
        self.delta_s_input.setValidator(QDoubleValidator(0, 10000, 2))
        yield_layout.addRow("Change in Substrate Concentration (ΔS) [g/L]:", self.delta_s_input)

        self.calculate_yield_button = QPushButton("Calculate Yield Coefficient")
        self.calculate_yield_button.clicked.connect(self.calculate_yield_coefficient)
        yield_layout.addRow(self.calculate_yield_button)

        yield_group.setLayout(yield_layout)
        input_layout.addWidget(yield_group)
        
        # Buttons Panel for Results
        buttons_layout = QHBoxLayout()
        
        # Clear button
        self.clear_button = QPushButton("Clear All")
        self.clear_button.clicked.connect(self.clear_all)
        buttons_layout.addWidget(self.clear_button)
        
        # Clear Results button
        self.clear_results_button = QPushButton("Clear Results")
        self.clear_results_button.clicked.connect(self.clear_results)
        buttons_layout.addWidget(self.clear_results_button)
        
        input_layout.addLayout(buttons_layout)

        # Results Section
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        results_layout.addWidget(self.results_text)
        
    def append_results(self, text):
        """Append text to the results with a timestamp and separator"""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        separator = "-" * 50
        
        # Get current text and append new results
        current_text = self.results_text.toPlainText()
        if current_text:
            new_text = f"{current_text}\n\n{separator}\n{current_time}\n{text}"
        else:
            new_text = f"{current_time}\n{text}"
        
        # Set the updated text and scroll to the bottom
        self.results_text.setPlainText(new_text)
        self.results_text.verticalScrollBar().setValue(
            self.results_text.verticalScrollBar().maximum()
        )

    @pyqtSlot()
    def calculate_feeding_rate(self):
        try:
            sf = float(self.sf_input.text())
            s = float(self.s_input.text())
            t = float(self.time_input.text())

            if t <= 0:
                self.append_results("Error: Time must be greater than zero.")
                return

            feeding_rate = (sf - s) / t
            self.append_results(f"Substrate Feeding Rate Results:\n\n"
                              f"Substrate Concentration in Feed (Sf): {sf:.2f} g/L\n"
                              f"Substrate Concentration in Reactor (S): {s:.2f} g/L\n"
                              f"Time (t): {t:.2f} h\n\n"
                              f"Substrate Feeding Rate (Fs): {feeding_rate:.4f} g/L·h")
        except ValueError:
            self.append_results("Error: Please enter valid numbers in all fields.")
        except Exception as e:
            self.append_results(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_biomass_concentration(self):
        try:
            x0 = float(self.x0_input.text())
            mu = float(self.mu_input.text())
            t = float(self.xt_time_input.text())

            biomass_concentration = x0 + (mu * x0 * t)
            self.append_results(f"Biomass Concentration Results:\n\n"
                              f"Initial Biomass Concentration (X0): {x0:.2f} g/L\n"
                              f"Specific Growth Rate (μ): {mu:.4f} h⁻¹\n"
                              f"Time (t): {t:.2f} h\n\n"
                              f"Biomass Concentration (Xt): {biomass_concentration:.4f} g/L")
        except ValueError:
            self.append_results("Error: Please enter valid numbers in all fields.")
        except Exception as e:
            self.append_results(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_product_formation_rate(self):
        try:
            dp = float(self.dp_input.text())
            dt = float(self.dt_input.text())

            if dt <= 0:
                self.append_results("Error: Change in time (dt) must be greater than zero.")
                return

            product_rate = dp / dt
            self.append_results(f"Product Formation Rate Results:\n\n"
                              f"Change in Product Concentration (dP): {dp:.2f} g/L\n"
                              f"Change in Time (dt): {dt:.2f} h\n\n"
                              f"Product Formation Rate (rp): {product_rate:.4f} g/L·h")
        except ValueError:
            self.append_results("Error: Please enter valid numbers in all fields.")
        except Exception as e:
            self.append_results(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_yield_coefficient(self):
        try:
            delta_x = float(self.delta_x_input.text())
            delta_s = float(self.delta_s_input.text())

            if delta_s == 0:
                self.append_results("Error: Change in substrate concentration (ΔS) must not be zero.")
                return

            yield_coefficient = delta_x / delta_s
            self.append_results(f"Yield Coefficient Results:\n\n"
                              f"Change in Biomass Concentration (ΔX): {delta_x:.2f} g/L\n"
                              f"Change in Substrate Concentration (ΔS): {delta_s:.2f} g/L\n\n"
                              f"Yield Coefficient (YX/S): {yield_coefficient:.4f} g/g")
        except ValueError:
            self.append_results("Error: Please enter valid numbers in all fields.")
        except Exception as e:
            self.append_results(f"Error: {str(e)}")
            
    @pyqtSlot()
    def clear_all(self):
        """Clear all input fields and results"""
        self.sf_input.clear()
        self.s_input.clear()
        self.time_input.clear()
        self.x0_input.clear()
        self.mu_input.clear()
        self.xt_time_input.clear()
        self.dp_input.clear()
        self.dt_input.clear()
        self.delta_x_input.clear()
        self.delta_s_input.clear()
        self.results_text.clear()
        
    @pyqtSlot()
    def clear_results(self):
        """Clear only the results text area"""
        self.results_text.clear()