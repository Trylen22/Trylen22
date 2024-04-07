# pressure_converter.py

def pressCon(value, from_unit, to_unit):
    # Conversions
    Conversions = {
        'Pa': 1,
        'kPa': 1000,
        'MPa': 1000000,
        'atm': 101325,
        'psi': 6894.75729,
        'lbf/ft2': 47.880259,
        'torr': 133.322368,
        'inHg': 3386.38867,
        'mmHg': 133.322368,
        'K': 1000
    }

    # Validity of unit check
    if from_unit not in Conversions or to_unit not in Conversions :
        return "Invalid unit"

    # Convert the value to Pascal (base unit)
    value_in_pascals = value * Conversions[from_unit]

    # Convert the value from Pascal to the desired unit
    result = value_in_pascals / Conversions[to_unit]

    return result

# Get user input for pressure value and units
user_input = input("Enter the pressure value and unit (e.g., 200 kPa): ")
pressure, from_unit = user_input.split()
pressure = float(pressure)

to_unit = input("Enter the output unit: ")

# Convert the pressure value
result = pressCon(pressure, from_unit, to_unit)

# Print the result
if isinstance(result, str):
    print(result)
else:
    print(f"{pressure} {from_unit} is equal to {result:.4f} {to_unit}")
