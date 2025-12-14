def f(n):
    arr = [15,38,7,23,14]
    if n in arr:
        return f'Result: number {n} appears in the array'
    else:
        return f'Result: number {n} not appears in the array'
    
print(f(15))
print(f(18))