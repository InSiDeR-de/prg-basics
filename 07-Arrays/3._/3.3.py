arr=[8,2,5,1,9]

r1='' 
r2='' 
for x in arr:
    r1+=f"{x} "

for y in arr:
    r2+=f"{y**2} "

print('Array:',r1)
print('2nd power:',r2)