with open('province.csv', encoding='UTF-8') as p:
    next(p)
    with open('vehicle.txt', encoding='UTF-8') as v:
        count = 0
        for line in p:
            lines=line.split(',')
            lines[1]=lines[1].strip()
            v.seek(0)
            for x in v:
                if x[0]==lines[0]:
                    count+=1
            print(f'{lines[1]}: {count}')
            count = 0

