###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
celcius = round(float(input("Enter temperature in degrees Celsius: ")),2)
farcostam = round((celcius * 9/5) + 32,2)
print(f'Temperature in degrees Fahrenheit: {farcostam}')