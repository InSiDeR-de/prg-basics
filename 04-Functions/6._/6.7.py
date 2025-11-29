def f(binary_number):
    for x in binary_number:
        if x == "0" or x == "1":
            result = True
            continue
        else:
            result = False
            break
    return result
    



if __name__ == "__main__":
    print(f'liczba 123124 jesr binarna? {f("123124")}')
    print(f'liczba 100000 jesr binarna? {f("100000")}')
    print(f'liczba 101010 jesr binarna? {f("101010")}')