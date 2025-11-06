###
# Program that simulates the operation of an electronic thermometer.
#

temperature = input("Enter the temperature in Celsius: ")
while True:
    if temperature.isdigit() == True:

        temperature = int(temperature)
        if temperature > 35:
            print("It is extermely hot")
            break
        elif temperature > 30:
            print("It is hot")
            break
        elif temperature > 15:
            print("It is warm")
            break
        elif temperature > 0:
            print("It is cold")
            break
        else:
            print("Warning! Freezing temperature!")
            break
    else:
        temperature = input("Invalid input. Please enter a numeric temperature value: ")