"""
Dilution Calculator module for bacterial culture OD calculations
"""
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, 
                            QLabel, QLineEdit, QPushButton, QTextEdit, QFormLayout)
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QDoubleValidator
import math

class DilutionCalculator(QWidget):
    """
    Calculator for bacterial culture dilutions and OD calculations
    """
    
    def __init__(self):
        """Initialize the dilution calculator tab"""
        super().__init__()
        
        # Create the input form
        self.create_widgets()
        
        # Apply styles to the widget
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
        """Create all the form widgets"""
        # Create form layout
        main_layout = QHBoxLayout(self)
        
        # Create left panel (inputs)
        input_group = QGroupBox("Inputs")
        input_layout = QVBoxLayout(input_group)
        
        # Create right panel (results)
        results_group = QGroupBox("Results")
        results_layout = QVBoxLayout(results_group)
        
        # Add panels to main layout
        main_layout.addWidget(input_group)
        main_layout.addWidget(results_group)

        # ------------ Dilution Factor Section ------------
        dilution_factor_group = QGroupBox("Dilution Factor Calculation")
        dilution_factor_layout = QFormLayout()

        # Volume of Sample
        self.sample_volume_input = QLineEdit()
        self.sample_volume_input.setValidator(QDoubleValidator(0, 10000, 2))
        self.sample_volume_input.setText("0.0")
        dilution_factor_layout.addRow("Volume of Sample (mL):", self.sample_volume_input)

        # Volume of Diluent
        self.diluent_volume_input = QLineEdit()
        self.diluent_volume_input.setValidator(QDoubleValidator(0, 10000, 2))
        self.diluent_volume_input.setText("0.0")
        dilution_factor_layout.addRow("Volume of Diluent (mL):", self.diluent_volume_input)

        # Calculate button
        self.calculate_dilution_factor_button = QPushButton("Calculate Dilution Factor")
        self.calculate_dilution_factor_button.clicked.connect(self.calculate_dilution_factor)
        dilution_factor_layout.addRow(self.calculate_dilution_factor_button)

        dilution_factor_group.setLayout(dilution_factor_layout)
        input_layout.addWidget(dilution_factor_group)

        # ------------ OD Calculation Section ------------
        od_group = QGroupBox("OD Calculation")
        od_layout = QFormLayout()
        
        # Absorbance
        self.absorbance_input = QLineEdit()
        self.absorbance_input.setValidator(QDoubleValidator(0, 100, 4))
        self.absorbance_input.setText("0.0")
        od_layout.addRow("Absorbance:", self.absorbance_input)
        
        # Dilution factor
        self.dilution_factor_input = QLineEdit()
        self.dilution_factor_input.setValidator(QDoubleValidator(0, 10000, 2))
        self.dilution_factor_input.setText("1.0")
        od_layout.addRow("Dilution factor:", self.dilution_factor_input)
        
        # Calculate button
        self.calculate_od_button = QPushButton("Calculate OD")
        self.calculate_od_button.clicked.connect(self.calculate_od)
        od_layout.addRow(self.calculate_od_button)
        
        od_group.setLayout(od_layout)
        input_layout.addWidget(od_group)
        
        # ------------ Dilution Section ------------
        dilution_group = QGroupBox("Dilution Preparation")
        dilution_layout = QFormLayout()
        
        # Current OD
        self.current_od_input = QLineEdit()
        self.current_od_input.setValidator(QDoubleValidator(0, 100, 4))
        self.current_od_input.setText("0.0")
        dilution_layout.addRow("Current OD:", self.current_od_input)
        
        # Target OD
        self.target_od_input = QLineEdit()
        self.target_od_input.setValidator(QDoubleValidator(0, 100, 4))
        self.target_od_input.setText("0.0")
        dilution_layout.addRow("Target OD:", self.target_od_input)
        
        # Final volume
        self.final_volume_input = QLineEdit()
        self.final_volume_input.setValidator(QDoubleValidator(0, 10000, 2))
        self.final_volume_input.setText("10.0")
        dilution_layout.addRow("Final volume (mL):", self.final_volume_input)
        
        # Calculate button
        self.calculate_dilution_button = QPushButton("Calculate Dilution")
        self.calculate_dilution_button.clicked.connect(self.calculate_dilution)
        dilution_layout.addRow(self.calculate_dilution_button)
        
        dilution_group.setLayout(dilution_layout)
        input_layout.addWidget(dilution_group)
        
        # ------------ Results Section ------------
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        results_layout.addWidget(self.results_text)
        
        # Clear button
        self.clear_button = QPushButton("Clear All")
        self.clear_button.clicked.connect(self.clear_all)
        input_layout.addWidget(self.clear_button)
    
    @pyqtSlot()
    def calculate_od(self):
        """Calculate the OD from absorbance and dilution factor"""
        try:
            absorbance = float(self.absorbance_input.text())
            dilution_factor = float(self.dilution_factor_input.text())
            
            od = absorbance * dilution_factor
            
            self.update_results(f"OD Calculation Results:\n\n"
                               f"Absorbance: {absorbance:.4f}\n"
                               f"Dilution Factor: {dilution_factor:.2f}\n"
                               f"Calculated OD: {od:.4f}")
            
            # Auto-fill the current OD field
            self.current_od_input.setText(f"{od:.4f}")
            
        except Exception as e:
            self.update_results(f"Error: {str(e)}\n\nPlease check your input values.")
    
    @pyqtSlot()
    def calculate_dilution(self):
        """Calculate the dilution factor needed to achieve the target OD and the volume to add."""
        try:
            current_od = float(self.current_od_input.text())
            target_od = float(self.target_od_input.text())
            final_volume = float(self.final_volume_input.text())

            if current_od <= 0:
                self.update_results("Error: Current OD must be greater than zero.")
                return

            if target_od >= current_od:
                self.update_results("Error: Target OD must be less than current OD for dilution.")
                return

            # Calculate dilution factor
            dilution_factor = current_od / target_od

            # Calculate the volume of the sample to add
            sample_volume = final_volume / dilution_factor

            # Calculate the volume of diluent to add
            diluent_volume = final_volume - sample_volume

            self.update_results(
                f"Dilution Factor Calculation Results:\n\n"
                f"Current OD: {current_od:.4f}\n"
                f"Target OD: {target_od:.4f}\n"
                f"Final Volume: {final_volume:.2f} mL\n\n"
                f"Dilution factor: 1:{dilution_factor:.2f}\n"
                f"Volume of Sample to Add: {sample_volume:.2f} mL\n"
                f"Volume of Diluent to Add: {diluent_volume:.2f} mL"
            )

        except Exception as e:
            self.update_results(f"Error: {str(e)}\n\nPlease check your input values.")
    
    @pyqtSlot()
    def calculate_dilution_factor(self):
        """Calculate the dilution factor based on sample and diluent volumes"""
        try:
            sample_volume = float(self.sample_volume_input.text())
            diluent_volume = float(self.diluent_volume_input.text())

            if sample_volume <= 0:
                self.update_results("Error: Volume of Sample must be greater than zero.")
                return

            # Calculate dilution factor
            dilution_factor = (sample_volume + diluent_volume) / sample_volume

            self.update_results(
                f"Dilution Factor Calculation Results:\n\n"
                f"Volume of Sample: {sample_volume:.2f} mL\n"
                f"Volume of Diluent: {diluent_volume:.2f} mL\n\n"
                f"Dilution Factor: {dilution_factor:.2f}"
            )

            # Auto-fill the dilution factor input for the next calculation
            self.dilution_factor_input.setText(f"{dilution_factor:.2f}")

        except Exception as e:
            self.update_results(f"Error: {str(e)}\n\nPlease check your input values.")
    
    def update_results(self, text):
        """Update the results text widget"""
        self.results_text.setPlainText(text)
    
    @pyqtSlot()
    def clear_all(self):
        """Clear all input fields and results"""
        self.absorbance_input.setText("0.0")
        self.dilution_factor_input.setText("1.0")
        self.current_od_input.setText("0.0")
        self.target_od_input.setText("0.0")
        self.final_volume_input.setText("10.0")
        self.results_text.clear()