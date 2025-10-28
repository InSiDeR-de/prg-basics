speed_str= input("Enter speed in km/h: ")
speed= float(speed_str)
valid_speed= 40 <= speed <= 140
print("Is the speed valid (0-140 km/h): ", valid_speed)