from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, 
                            QLabel, QLineEdit, QPushButton, QTextEdit, QFormLayout, QTabWidget)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QDoubleValidator
import datetime

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

        # Dilution Rate Section
        dilution_rate_group = QGroupBox("Dilution Rate Calculation")
        dilution_rate_layout = QFormLayout()

        self.flow_rate_input = QLineEdit()
        self.flow_rate_input.setValidator(QDoubleValidator(0, 10000, 2))
        dilution_rate_layout.addRow("Flow Rate (F) [L/h]:", self.flow_rate_input)

        self.volume_input = QLineEdit()
        self.volume_input.setValidator(QDoubleValidator(0, 10000, 2))
        dilution_rate_layout.addRow("Volume (V) [L]:", self.volume_input)

        self.calculate_dilution_rate_button = QPushButton("Calculate Dilution Rate")
        self.calculate_dilution_rate_button.clicked.connect(self.calculate_dilution_rate)
        dilution_rate_layout.addRow(self.calculate_dilution_rate_button)

        dilution_rate_group.setLayout(dilution_rate_layout)
        input_layout.addWidget(dilution_rate_group)

        # Steady-State Biomass Concentration Section
        biomass_group = QGroupBox("Steady-State Biomass Concentration")
        biomass_layout = QFormLayout()

        self.mu_max_input = QLineEdit()
        self.mu_max_input.setValidator(QDoubleValidator(0, 100, 4))
        biomass_layout.addRow("Maximum Specific Growth Rate (μmax) [h⁻¹]:", self.mu_max_input)

        self.ss_substrate_input = QLineEdit()
        self.ss_substrate_input.setValidator(QDoubleValidator(0, 10000, 2))
        biomass_layout.addRow("Steady-State Substrate Concentration (Sss) [g/L]:", self.ss_substrate_input)

        self.ks_input = QLineEdit()
        self.ks_input.setValidator(QDoubleValidator(0, 10000, 2))
        biomass_layout.addRow("Half-Saturation Constant (Ks) [g/L]:", self.ks_input)

        self.calculate_biomass_button = QPushButton("Calculate Biomass Concentration")
        self.calculate_biomass_button.clicked.connect(self.calculate_biomass_concentration)
        biomass_layout.addRow(self.calculate_biomass_button)

        biomass_group.setLayout(biomass_layout)
        input_layout.addWidget(biomass_group)

        # Substrate Utilization Rate Section
        substrate_group = QGroupBox("Substrate Utilization Rate")
        substrate_layout = QFormLayout()

        self.sin_input = QLineEdit()
        self.sin_input.setValidator(QDoubleValidator(0, 10000, 2))
        substrate_layout.addRow("Substrate Concentration in Feed (Sin) [g/L]:", self.sin_input)

        self.ss_substrate_util_input = QLineEdit()
        self.ss_substrate_util_input.setValidator(QDoubleValidator(0, 10000, 2))
        substrate_layout.addRow("Steady-State Substrate Concentration (Sss) [g/L]:", self.ss_substrate_util_input)

        self.ss_biomass_input = QLineEdit()
        self.ss_biomass_input.setValidator(QDoubleValidator(0, 10000, 2))
        substrate_layout.addRow("Steady-State Biomass Concentration (Xss) [g/L]:", self.ss_biomass_input)

        self.calculate_substrate_button = QPushButton("Calculate Substrate Utilization Rate")
        self.calculate_substrate_button.clicked.connect(self.calculate_substrate_utilization_rate)
        substrate_layout.addRow(self.calculate_substrate_button)

        substrate_group.setLayout(substrate_layout)
        input_layout.addWidget(substrate_group)

        # Productivity Section
        productivity_group = QGroupBox("Productivity")
        productivity_layout = QFormLayout()

        self.ss_product_input = QLineEdit()
        self.ss_product_input.setValidator(QDoubleValidator(0, 10000, 2))
        productivity_layout.addRow("Steady-State Product Concentration (Pss) [g/L]:", self.ss_product_input)

        self.calculate_productivity_button = QPushButton("Calculate Productivity")
        self.calculate_productivity_button.clicked.connect(self.calculate_productivity)
        productivity_layout.addRow(self.calculate_productivity_button)

        productivity_group.setLayout(productivity_layout)
        input_layout.addWidget(productivity_group)

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
    def calculate_dilution_rate(self):
        try:
            flow_rate = float(self.flow_rate_input.text())
            volume = float(self.volume_input.text())

            if volume <= 0:
                self.append_results("Error: Volume must be greater than zero.")
                return

            dilution_rate = flow_rate / volume
            self.append_results(f"Dilution Rate Calculation Results:\n\n"
                              f"Flow Rate (F): {flow_rate:.2f} L/h\n"
                              f"Volume (V): {volume:.2f} L\n\n"
                              f"Dilution Rate (D): {dilution_rate:.4f} h⁻¹")
        except ValueError:
            self.append_results("Error: Please enter valid numbers in all fields.")
        except Exception as e:
            self.append_results(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_biomass_concentration(self):
        try:
            mu_max = float(self.mu_max_input.text())
            ss_substrate = float(self.ss_substrate_input.text())
            ks = float(self.ks_input.text())

            biomass_concentration = (mu_max * ss_substrate) / (ks + ss_substrate)
            self.append_results(f"Biomass Concentration Results:\n\n"
                              f"Maximum Specific Growth Rate (μmax): {mu_max:.4f} h⁻¹\n"
                              f"Steady-State Substrate Concentration (Sss): {ss_substrate:.2f} g/L\n"
                              f"Half-Saturation Constant (Ks): {ks:.2f} g/L\n\n"
                              f"Steady-State Biomass Concentration (Xss): {biomass_concentration:.4f} g/L")
        except ValueError:
            self.append_results("Error: Please enter valid numbers in all fields.")
        except Exception as e:
            self.append_results(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_substrate_utilization_rate(self):
        try:
            dilution_rate = float(self.flow_rate_input.text()) / float(self.volume_input.text())
            sin = float(self.sin_input.text())
            ss_substrate = float(self.ss_substrate_util_input.text())
            ss_biomass = float(self.ss_biomass_input.text())

            substrate_utilization_rate = dilution_rate * (sin - ss_substrate) * ss_biomass
            self.append_results(f"Substrate Utilization Rate Results:\n\n"
                              f"Substrate Concentration in Feed (Sin): {sin:.2f} g/L\n"
                              f"Steady-State Substrate Concentration (Sss): {ss_substrate:.2f} g/L\n"
                              f"Steady-State Biomass Concentration (Xss): {ss_biomass:.2f} g/L\n"
                              f"Dilution Rate (D): {dilution_rate:.4f} h⁻¹\n\n"
                              f"Substrate Utilization Rate (rs): {substrate_utilization_rate:.4f} g/L·h")
        except ValueError:
            self.append_results("Error: Please enter valid numbers in all fields.")
        except Exception as e:
            self.append_results(f"Error: {str(e)}")

    @pyqtSlot()
    def calculate_productivity(self):
        try:
            dilution_rate = float(self.flow_rate_input.text()) / float(self.volume_input.text())
            ss_product = float(self.ss_product_input.text())

            productivity = dilution_rate * ss_product
            self.append_results(f"Productivity Results:\n\n"
                              f"Steady-State Product Concentration (Pss): {ss_product:.2f} g/L\n"
                              f"Dilution Rate (D): {dilution_rate:.4f} h⁻¹\n\n"
                              f"Productivity (P): {productivity:.4f} g/L·h")
        except ValueError:
            self.append_results("Error: Please enter valid numbers in all fields.")
        except Exception as e:
            self.append_results(f"Error: {str(e)}")
            
    @pyqtSlot()
    def clear_all(self):
        """Clear all input fields and results"""
        self.flow_rate_input.clear()
        self.volume_input.clear()
        self.mu_max_input.clear()
        self.ss_substrate_input.clear()
        self.ks_input.clear()
        self.sin_input.clear() 
        self.ss_substrate_util_input.clear()
        self.ss_biomass_input.clear()
        self.ss_product_input.clear()
        self.results_text.clear()
        
    @pyqtSlot()
    def clear_results(self):
        """Clear only the results text area"""
        self.results_text.clear()