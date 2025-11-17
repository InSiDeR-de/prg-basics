def sum_digits(number):
    
    ab= abs(any_number)
    st = str(ab)
    x=0
    for char in st:
        d=int(char)
        x+=d
    return x

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')