def f(n):
    a, b = 0, 1
    seq=[]
    x=0
    while x<n:
        seq.append(a)
        a,b = b ,a+b
        x+=1
    return seq[n-1]
        



if __name__ == "__main__":
    print(f(5))
    print(f(9))
    print(f(6))