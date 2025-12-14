arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

max_len=0
res=''
for x in arr:
    res+=f'{x} '
    if len(x)>max_len:
        max_len=len(x)
        max_arr=x
    else: continue
print('names: ',res)
print('Longest name: ', max_arr)
