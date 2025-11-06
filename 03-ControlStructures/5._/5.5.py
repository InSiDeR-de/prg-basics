###
# Sums numbers entered by user
#
total_sum = 0
i=0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    i += 1
    total_sum += number
    arithmetic_mean = total_sum / i

print(f"The total sum of the numbers is: {total_sum} and the arithmetic mean is: {arithmetic_mean}")