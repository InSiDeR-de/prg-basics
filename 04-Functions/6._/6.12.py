def f(n):
    result="*"
    if n==1:
        return result
    else:
        n-=1
        while n>0:
            result+="/*"
            n-=1
        return result





if __name__ == "__main__":
    print(f(4))
    print(f(1))
    print(f(3))