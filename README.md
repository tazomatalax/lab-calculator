# Lab Calculator

Lab Calculator is a GUI application for performing common laboratory calculations. It is built using PyQt5 and includes the following features:

- **Dilution Calculator**: Calculate bacterial culture dilutions and OD values.
- **C1V1 Calculator**: Perform C1V1 = C2V2 calculations to determine missing values.
- **Continuous Bioreactor Calculator**: Calculate key parameters for continuous bioreactor operation.
- **Fed-Batch Bioreactor Calculator**: Perform calculations for fed-batch bioreactor processes.

## Features

### Dilution Calculator
- Input absorbance and dilution factor to calculate OD.
- Input current OD, target OD, and final volume to calculate dilution volumes.

### C1V1 Calculator
- Input any three values (C1, V1, C2, V2) to calculate the missing value.

### Continuous Bioreactor Calculator
- **Dilution Rate**: Calculate dilution rate from flow rate and reactor volume.
- **Biomass Concentration**: Determine steady-state biomass concentration using Monod kinetics.
- **Substrate Utilization Rate**: Calculate substrate utilization rate based on feed and reactor conditions.
- **Productivity**: Compute the overall productivity of the bioreactor.

### Fed-Batch Bioreactor Calculator
- **Substrate Feeding Rate**: Calculate the rate at which substrate should be fed.
- **Biomass Concentration**: Predict biomass concentration over time based on growth parameters.
- **Product Formation Rate**: Determine the rate of product formation in the bioreactor.
- **Yield Coefficient**: Calculate the yield of biomass per substrate consumed.

## Styling
The application uses a consistent material theme with the following styling:
- Rounded green buttons.
- Styled input fields with light backgrounds and rounded borders.
- Group boxes with green borders and bold titles.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Example Usage
### Dilution Calculator
1. Enter absorbance and dilution factor.
2. Click "Calculate OD" to compute the OD.

### C1V1 Calculator
1. Enter any three values (e.g., C1, V1, C2).
2. Click "Calculate" to compute the missing value (e.g., V2).

### Continuous Bioreactor Calculator
1. Enter flow rate and volume to calculate dilution rate.
2. Enter kinetic parameters to determine steady-state biomass concentration.

### Fed-Batch Bioreactor Calculator
1. Enter substrate concentrations and time to calculate feeding rate.
2. Input growth parameters to predict biomass concentration over time.

## Building an Executable
To build a standalone executable:
```bash
python build_exe.py
```
This will create a standalone executable in the `build/LabCalculator` directory.

## AI Assistant Prompts
Below are example prompts that could be used with an AI coding assistant to recreate this project:

1. **Initial Setup**:
   ```
   Create a PyQt5 GUI application for laboratory calculations. Include separate modules for dilution calculations, C1V1 calculations, continuous bioreactor calculations, and fed-batch bioreactor calculations. Use a consistent green material theme for the UI.
   ```

2. **Dilution Calculator Module**:
   ```
   Create a PyQt5 module for a dilution calculator that can calculate OD values from absorbance and dilution factor, and calculate dilution volumes from current OD, target OD, and final volume.
   ```

3. **C1V1 Calculator Module**:
   ```
   Implement a C1V1=C2V2 calculator as a PyQt5 widget that allows the user to enter any three values and calculate the fourth.
   ```

4. **Continuous Bioreactor Calculator**:
   ```
   Create a PyQt5 widget for continuous bioreactor calculations that includes calculating dilution rate, steady-state biomass concentration using Monod kinetics, substrate utilization rate, and productivity.
   ```

5. **Fed-Batch Bioreactor Calculator**:
   ```
   Implement a fed-batch bioreactor calculator PyQt5 widget with functionality to calculate substrate feeding rate, biomass concentration over time, product formation rate, and yield coefficient.
   ```

6. **Main Application Integration**:
   ```
   Create a main.py file that integrates all calculator modules into a tabbed interface. Add a consistent theme with green buttons, styled input fields with light backgrounds and rounded borders, and group boxes with green borders.
   ```

7. **Building Executable**:
   ```
   Create a build script using PyInstaller to package the lab calculator application as a standalone executable.
   ```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

## License
This project is licensed under the MIT License.