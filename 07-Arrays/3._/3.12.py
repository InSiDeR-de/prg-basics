arr=[2,3,2,5,8,1,9,8]
res=''
ar=''
for x in arr:
    ar+=f'{x} '
    if arr.count(x)>1:
        continue
    else:
        res+=f'{x} '
print('Array:',ar)
print('Unique elements:', res)