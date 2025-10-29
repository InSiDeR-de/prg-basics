# A program that prints your height both in cm and in feet and inches.
cm = int(input("Enter your height in cm: "))

# convert cm to total inches
total_inches = cm / 2.54
total_inches_int = int(total_inches)  # drop fractional part

# calculate feet and remaining inches using integer division and remainder
feet = total_inches_int // 12
inches = total_inches_int % 12

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')