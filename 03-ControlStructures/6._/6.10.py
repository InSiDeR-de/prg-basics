dogage = int(input('Enter dog age in years: '))
if dogage <= 2:
    humanage = dogage * 10.5
else:
    humanage = 21 + (dogage - 2) * 4
print(f'The dog age in human years is: {humanage} years')
