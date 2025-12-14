with open('it_company.csv') as file:
    i=0
    for lines in file:
        if i%6!=0:
            print(lines)
            i+=1
        else:
            a = input('Press Enter key to continue or type q to quit: ')
            if a.lower()=='q':
                break
            i+=1


