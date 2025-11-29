def f(product_code):
    sum = int(product_code[0])+ int(product_code[1])+ int(product_code[2])
    result = sum%7
    if product_code[3] == str(result):
        return True
    else:
        return False



if __name__ == "__main__":
    print(f('1082'))
    print(f('2035'))
    print(f('1114'))