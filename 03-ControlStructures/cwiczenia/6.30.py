def f(a):
    licznik = int(a**0.5)

    i=1

    result =""
    for i in range(1, licznik+1):
        z=1
        for z in range(1, licznik+1):
            result +=f"{i*z} "           
            z+=1
        print(result)
        result=""
        i+=1
if __name__ == "__main__":
    print(f(64))







