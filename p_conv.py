# pressure_converter.py

def pressCon(value, from_unit, to_unit):
    factors = {
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

    if from_unit not in factors or to_unit not in factors:
        return "Invalid unit"

    value_in_pascals = value * factors[from_unit]
    result = value_in_pascals / factors[to_unit]

    return result