def f(x,y):
    result = 0
    for z in range(x,y):
        if z<0 and z%2==0:
            result+=1
        else:
            continue
    return result








if __name__ == "__main__":
    print(f(-7,8))
    print(f(-1,11))
    print(f(-2,1))