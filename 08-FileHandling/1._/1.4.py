with open('countries.txt', 'r') as file:
    content = file.read()
    for line in content:
        print(line, end='')