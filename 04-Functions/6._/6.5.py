def f(x,y,z):
    if x in range(y,z):
        return "Yes"
    else:
        return "No"
    

if __name__ == "__main__":
    print('Czy liczba 5 jest w przedziale 1 do 10?', f(5,1,10))
    print('Czy liczba 15 jest w przedziale 1 do 10?', f(15,1,10))
    print('Czy liczba -3 jest w przedziale -5 do 0?', f(-3,-5,0))