# Lab Calculator

A simple Python-based GUI calculator for laboratory calculations such as dilutions for determining OD of bacterial cultures. The application is built with PyQt5 and can be compiled into a standalone executable.

## Features

- **Dilution Calculator**: Calculate the volumes needed to prepare dilutions of bacterial cultures
- **OD Calculator**: Calculate optical density from absorbance readings and dilution factors
- **Extensible Design**: Easily add new calculation modules
- **Cross-platform**: Works on Windows, macOS, and Linux (when built for the respective platform)
- **Standalone Executable**: Can be distributed as a single .exe file

## Installation

### From Source

1. Clone or download this repository
2. Ensure Python 3.6+ is installed
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python main.py
   ```

### As Executable

1. Download the latest LabCalculator.exe from the releases page
2. Run the executable - no installation required

## Building the Executable

To build the standalone executable:

```
python build_exe.py
```

The executable will be created in the `dist` folder.

## Extending the Calculator

The Lab Calculator is designed to be easily extensible with new calculation modules. Each module is a separate Python file in the `calc_modules` directory.

### Adding a New Calculation Module

1. Create a new Python file in the `calc_modules` directory, e.g., `my_calculator.py`
2. Implement a class that inherits from `QWidget`
3. Include the necessary calculation logic and UI components
4. Import and add the new module in `main.py`

### Module Structure

Each module should:
1. Create a class that inherits from `QWidget`
2. Implement a UI with input fields, calculation buttons, and result display
3. Handle calculation logic and error handling

### Importing Your New Module

After creating your module, update `main.py` to include it:

```python
from calc_modules import dilution_calculator, my_calculator  # Add your module

# In the LabCalculatorApp.__init__ method:
self.my_tab = my_calculator.MyCalculator()
self.tab_widget.addTab(self.my_tab, "My Calculator")  # Add a new tab
```

## Prompt Template for LLM Code Generation

When requesting code for new calculation modules from AI coding assistants, use the following prompt template:

```
Create a new calculation module for the Lab Calculator application that [describe specific calculation functionality].

The module should follow this structure:
1. A Python class inheriting from QWidget
2. Input fields for [list specific input parameters]
3. Calculation buttons
4. Results display area
5. Error handling for invalid inputs

Here's the basic template from existing modules:
- Uses PyQt5 for the UI
- Includes form layout with input fields and validation
- Has calculation methods with proper error handling
- Displays formatted results

The specific calculations should include [describe the scientific formulas and logic].

The file should be saved as `[module_name].py` in the `calc_modules` directory.
```

## Example Module: Solution Preparation Calculator

For example, to request a solution preparation calculator module:

```
Create a new calculation module for the Lab Calculator application that calculates amounts needed for preparing laboratory solutions.

The module should follow this structure:
1. A Python class inheriting from QWidget
2. Input fields for: desired concentration, desired volume, stock concentration, molecular weight
3. Calculation buttons for both solid and liquid stock preparations
4. Results display area
5. Error handling for invalid inputs

Here's the basic template from existing modules:
- Uses PyQt5 for the UI
- Includes form layout with input fields and validation
- Has calculation methods with proper error handling
- Displays formatted results

The specific calculations should include:
- For solid reagents: mass(g) = (concentration(mol/L) * volume(L) * molecular weight(g/mol))
- For liquid stocks: volume of stock(mL) = (desired concentration * desired volume) / stock concentration

The file should be saved as `solution_calculator.py` in the `calc_modules` directory.
```

## License

MIT License

## Contributing

Contributions are welcome. Please feel free to submit a Pull Request.