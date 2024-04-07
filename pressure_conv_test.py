# test.py

import pressure_converter as pc

# Get user input for pressure value and units
user_input = input("Enter the pressure value and unit (e.g., 200 kPa): ")
pressure, from_unit = user_input.split()
pressure = float(pressure)

to_unit = input("Enter the output unit: ")

# Convert the pressure value
result = pc.pressCon(pressure, from_unit, to_unit)

# Print the result
if isinstance(result, str):
    print(result)
else:
    print(f"{pressure} {from_unit} is equal to {result:.4f} {to_unit}")