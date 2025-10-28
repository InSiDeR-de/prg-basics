import math
circumference = float(input("Enter the circumference of the tree in cm: "))
diameter = circumference / math.pi
can_be_cut_down = diameter >= 50
print('Tree can be cut down: ', can_be_cut_down)
print('Diameter of the tree: ', diameter)
