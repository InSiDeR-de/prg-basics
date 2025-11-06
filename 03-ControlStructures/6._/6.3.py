###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = True # False - switch off, True - switch on
light_switch2 = False  # False - switch off, True - switch on
bulbs_on = 0
if light_switch1 and light_switch2:
    bulbs_on += 2
elif light_switch1 or light_switch2:
    bulbs_on += 1
else:
    bulbs_on += 0
print(f"Number of bulbs illuminating the house: {bulbs_on}")
