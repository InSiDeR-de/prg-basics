# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food_exp=0
transport_exp = 0 
utilities_exp = 0
month = []
total_expenses = 0
for week in monthly_expenses:
    food_exp += week[0]
    transport_exp += week[1]
    utilities_exp += week[2]
    total_expenses = food_exp + transport_exp + utilities_exp
    month.append(week[0] + week[1] + week[2])






# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food_exp)
print('Transport:',transport_exp)
print('Utilities:',utilities_exp)
print('Week 1:',month[0])
print('Week 2:',month[1])
print('Week 3:',month[2])
print('Week 4:',month[3])
print('---------------')
print('TOTAL:',total_expenses)