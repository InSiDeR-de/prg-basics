age = input("Enter your age: ")
while True:
    if age.isdigit() == True:
        age = int(age)
        if age < 0:
            print("Age cannot be negative.")
            break
        elif age < 13:
            print("You are a child.")
            break
        elif age <= 19:
            print("You are a teenager.")
            break
        elif age <= 64:
            print("You are an adult.")
            break
        else:
            print("You are a senior.")
            break
    else:
        age = input("Invalid input. Please enter a numeric value for age: ")