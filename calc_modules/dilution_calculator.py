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
        """Calculate the volumes needed for a dilution"""
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
            
            # Calculate culture volume and diluent volume
            culture_volume = (target_od / current_od) * final_volume
            diluent_volume = final_volume - culture_volume
            
            # Calculate dilution factor
            dilution_factor = current_od / target_od
            
            self.update_results(
                f"Dilution Results:\n\n"
                f"Current OD: {current_od:.4f}\n"
                f"Target OD: {target_od:.4f}\n"
                f"Final volume: {final_volume:.2f} mL\n\n"
                f"Add {culture_volume:.2f} mL of culture\n"
                f"Add {diluent_volume:.2f} mL of diluent\n\n"
                f"Dilution factor: 1:{dilution_factor:.2f}"
            )
            
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