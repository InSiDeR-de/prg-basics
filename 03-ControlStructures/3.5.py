###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12): '))

if  month == 2:
    days = 28 ## months with 28 days
elif month in [4, 6, 9, 11]:
    days = 30 ## months with 30 days
else:
    days = 31

print(f'Month {month} has {days} days')