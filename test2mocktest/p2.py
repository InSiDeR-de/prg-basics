def f(arr):
    for x in arr:
        if arr.count(x)>1:
            continue
        return x




if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))
    print(f([5,5,5,5,5,5,7]))