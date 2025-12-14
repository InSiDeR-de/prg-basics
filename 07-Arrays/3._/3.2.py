arr=[15, 8, 31, 47, 2, 19]
result=''
result2=''
for x in arr:
    result +=f'{x} '
for y in reversed(arr):
    result2 +=f'{y} '

print('existed array: ', result)
print('reverse array: ', result2)