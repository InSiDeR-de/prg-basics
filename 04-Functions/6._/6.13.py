def f(n):
    result=''
    for x in range(0,n+1):
        result+=f'{x}'
    return result




if __name__ == "__main__":
    print(f(11))
    print(f(4))
    print(f(10))