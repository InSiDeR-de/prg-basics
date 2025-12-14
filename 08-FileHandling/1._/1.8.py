with open('pets.txt', 'r') as file:
    total=0
    for lines in file:
        worlds=lines.split(' ')
        total+=len(worlds)
print(total)