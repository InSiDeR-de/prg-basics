def f(name):

    return name.count('e')


if __name__ == "__main__":
    print('Liczba liter e w słowie "elementarne" to', f('elementarne'))
    print('Liczba liter e w słowie "energetyczne" to', f('energetyczne'))
    print('Liczba liter e w słowie "programowanie" to', f('programowanie'))