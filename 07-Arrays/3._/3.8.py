def star(n):
    res=f'{n}: '
    for x in range(0,n):
        res+="*"
    return res

if __name__ == "__main__":
    print(star(2))
    print(star(3))
    print(star(10))