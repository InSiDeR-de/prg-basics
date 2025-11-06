park_hours = input("Enter the number of hours you park: ")
while True:
    if park_hours.isdigit() == True:
        park_hours = int(park_hours)
        if park_hours <= 2:
            fee = 5
        elif park_hours <= 6:
            fee = 15
        else:
            fee = 20
        print(f"The parking fee is: €{fee}")
        break
    else:
        park_hours = input("Invalid input. Please enter a numeric value for parking hours: ")