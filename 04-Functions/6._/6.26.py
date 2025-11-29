def f(text):
    result=''
    i=0
    for x in text:
        i+=1
        if i==1:
            result+=f"{x}"
        else:
            result+=f"-{x}"
    return result



if __name__ == "__main__":
    print(f("University"))
    print(f("UE"))
    print(f("x"))