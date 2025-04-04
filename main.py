#!/usr/bin/env python3
"""
Lab Calculator - A GUI calculator for common laboratory calculations
"""
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QStatusBar, QAction, QMessageBox
from calc_modules import dilution_calculator
from calc_modules import c1v1_calculator
from calc_modules.continuous_bioreactor_calculator import ContinuousBioreactorCalculator
from calc_modules.fed_batch_bioreactor_calculator import FedBatchBioreactorCalculator

class LabCalculatorApp(QMainWindow):
    """Main application class for the Lab Calculator"""
    
    def __init__(self):
        """Initialize the application"""
        super().__init__()
        self.setWindowTitle("Lab Calculator")
        self.setGeometry(200, 50, 800, 1000)
        self.setMinimumSize(550, 450)
        
        # Create central widget with layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Create notebook for different calculator tabs
        self.tab_widget = QTabWidget()
        self.main_layout.addWidget(self.tab_widget)
        
        # Create the dilution calculator tab
        self.dilution_tab = dilution_calculator.DilutionCalculator()
        self.tab_widget.addTab(self.dilution_tab, "Dilution Calculator")
        
        # Create the C1V1 calculator tab
        self.c1v1_tab = c1v1_calculator.C1V1Calculator()
        self.tab_widget.addTab(self.c1v1_tab, "C1V1 Calculator")
        
        # Create the continuous bioreactor calculator tab
        self.continuous_bioreactor_tab = ContinuousBioreactorCalculator()
        self.tab_widget.addTab(self.continuous_bioreactor_tab, "Continuous Bioreactor")
        
        # Create the fed-batch bioreactor calculator tab
        self.fed_batch_bioreactor_tab = FedBatchBioreactorCalculator()
        self.tab_widget.addTab(self.fed_batch_bioreactor_tab, "Fed-Batch Bioreactor")
        
        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        # Create menu
        self.create_menu()
    
    def create_menu(self):
        """Create the application menu"""
        menu_bar = self.menuBar()
        
        # File menu
        file_menu = menu_bar.addMenu("&File")
        exit_action = QAction("E&xit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Help menu
        help_menu = menu_bar.addMenu("&Help")
        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def show_about(self):
        """Display the about dialog"""
        QMessageBox.information(
            self,
            "About Lab Calculator",
            "Lab Calculator v1.0\n\n"
            "A simple calculator for common laboratory calculations.\n"
            "Easily extensible for additional calculations."
        )

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def main():
    """Main function to start the application"""
    app = QApplication(sys.argv)
    window = LabCalculatorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()