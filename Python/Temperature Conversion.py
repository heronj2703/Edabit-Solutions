# Write a program that takes a temperature input in celsius and converts it to Fahrenheit and Kelvin.
# Return the converted temperature values in a list.

def temp_conversion(celsius):
    return 'Invalid' if round(celsius + 273.15, 2) < 0 else [round(celsius * 9 / 5 + 32, 2), round(celsius + 273.15, 2)]
