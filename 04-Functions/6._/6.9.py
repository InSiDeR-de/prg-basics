def f(number, even):
    result=0
    number=str(number)
    for x in number:
        x = int(x)
        if even == True:
            if x%2==0:
                result+=x
            else:
                continue
        else:
            if x%2!=0:
                result+=x
            else:
                continue
    return result

        



if __name__ == "__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))