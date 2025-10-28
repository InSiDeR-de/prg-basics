###
# A program to calculate the volume and surface area of ​​a cube.
# 
sidea_string = input('Enter cuboid side a: ')
sideb_string = input('Enter cuboid side b: ')
sidec_string = input('Enter cuboid side c: ')
sidea = int(sidea_string)
sideb = int(sideb_string)
sidec = int(sidec_string)
cuboid_volume = sidea * sideb * sidec
cuboid_surface_area = 2*(sidea*sideb)+2*(sideb*sidec)+2*(sidec*sidea)
print(f'The volume of a cube with sides: a={sidea} b={sideb} c={sidec} is {cuboid_volume}')
print(f'The surface area of a cube with side: a={sidea} b={sideb} c={sidec} is {cuboid_surface_area}')