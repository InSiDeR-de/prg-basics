arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
i=1
j=1
for x in arr:
    for y in x:
        x[j-1]+=i*j
        print(f'{x[j-1]}', end=' ')
        j+=1
    i+=1
    j=1
    print()
i=+1
    