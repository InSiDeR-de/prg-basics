arr=[[-38, 19], 
     [5,40],
     [-7,11],
     [29,16]]
max_value=0

for x in arr:
    for y in x:
        if y>max_value:
            max_value=y
            
row=0
for x in arr:
    
    col=0
    for y in x:
        col+=1
        if y == max_value:

            break
        else: 
            continue
    row+=1
    break
    
            
        
print(max_value)
print(row)
print(col)
        
    