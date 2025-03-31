# Lab Calculator

Lab Calculator is a GUI application for performing common laboratory calculations. It is built using PyQt5 and includes the following features:

- **Dilution Calculator**: Calculate bacterial culture dilutions and OD values.
- **C1V1 Calculator**: Perform C1V1 = C2V2 calculations to determine missing values.

## Features

### Dilution Calculator
- Input absorbance and dilution factor to calculate OD.
- Input current OD, target OD, and final volume to calculate dilution volumes.

### C1V1 Calculator
- Input any three values (C1, V1, C2, V2) to calculate the missing value.

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

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

## License
This project is licensed under the MIT License.