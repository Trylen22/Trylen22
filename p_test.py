# test.py

import p_conv as pc

pressure = 200
units = ['Pa', 'kPa', 'MPa', 'atm', 'psi', 'lbf/ft2', 'torr', 'inHg', 'mmHg']

print("{:<10} {:<10} {:<20}".format('Input Unit', 'Output Unit', 'Value'))
print("-" * 40)

for input_unit in units:
    for output_unit in units:
        value = pc.pressCon(pressure, input_unit, output_unit)
        print("{:<10} {:<10} {:<20}".format(input_unit, output_unit, value))
    print()