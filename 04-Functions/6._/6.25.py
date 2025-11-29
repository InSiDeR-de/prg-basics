def f(x,y):
    result=0
    for z in range(x,y+1):
        if z%2==0 and z%3==0 and z%4!=0:
            result+=z
        else:
            continue
    return result

if __name__ == "__main__":
    print(f(1,20))
    print(f(10,30))
    print(f(20,21))