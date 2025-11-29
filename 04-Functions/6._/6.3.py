def f(name):
    name-=1
    nazwy = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec',
             'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']
    return nazwy[name]



if __name__ == "__main__":
    print('Numer miesiąca 3 to', f(3))
    print('Numer miesiąca 5 to', f(5))
    print('Numer miesiąca 6 to', f(6))

    