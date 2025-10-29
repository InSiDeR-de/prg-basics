###
# Calculation of circle area and circumference 
#   
import math
input = round(float(input("Enter circle radius: ")),2)
area = round(math.pi * input**2,2)
circumference = round(2 * math.pi * input,2)
print(f'Circle area: {area}')
print(f'Circle circumference: {circumference}') 