array = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
i=0
for x in array:
    x[i]+=1
    i+=1
    for y in x:
        print(y,end=" ")
    print()
