def length_converter(value, from_unit, to_unit):
    units = {'m': 1, 'cm': 0.01, 'mm': 0.001, 'km': 1000}
    
    return value * units[from_unit] / units[to_unit]

def weight_converter(value, from_unit, to_unit):
    units = {'g': 1, 'mg': 0.001, 'kg': 1000, 'lb': 453.592}
    return value * units[from_unit] / units[to_unit]

def distance_converter(value, from_unit, to_unit):
    units = {'m': 1, 'km': 1000, 'mi': 1609.34}
    return value * units[from_unit] / units[to_unit]

def speed_converter(value, from_unit, to_unit):
    units = {'m/s': 1, 'km/s': 1000}
    return value * units[from_unit] / units[to_unit]

# Get input from user
unit_type = input("Enter the type of unit (length/weight/distance/speed): ")
value = float(input("Enter the value to convert: "))


if unit_type == "length":
    
    from_unit = input("Enter the unit of length (m/cm/mm/km): ")
    to_unit = input("Enter the unit to convert to (m/cm/mm/km): ")
    result = length_converter(value, from_unit, to_unit)
    print(f"{value} {from_unit} is equal to {result} {to_unit}")

elif unit_type == "weight":
    
    from_unit = input("Enter the unit of weight (g/mg/kg/lb): ")
    to_unit = input("Enter the unit to convert to (g/mg/kg/lb): ")
    result = weight_converter(value, from_unit, to_unit)
    print(f"{value} {from_unit} is equal to {result} {to_unit}")

elif unit_type == "distance":
    
    from_unit = input("Enter the unit of distance (m/km/mi): ")
    to_unit = input("Enter the unit to convert to (m/km/mi): ")
    result = distance_converter(value, from_unit, to_unit)
    print(f"{value} {from_unit} is equal to {result} {to_unit}")

elif unit_type == "speed":
    
    from_unit = input("Enter the unit of speed (m/s/km/s): ")
    to_unit = input("Enter the unit to convert to (m/s/km/s): ")
    result = speed_converter(value, from_unit, to_unit)
    print(f"{value} {from_unit} is equal to {result} {to_unit}")

else:
    print("Invalid unit type. Please enter 'length', 'weight', 'distance', or 'speed'.")

