def f(detector):
    inn = 0
    out =0
    for x in detector:
        if x =='+':
            inn+=1
        else:
            out +=1
    return 


    



if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))