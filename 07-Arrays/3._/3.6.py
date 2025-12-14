arr=[15, 8, 31, 47, 2, 19]
i=0
sum=0
res=''
while i<len(arr):
    res+=f'{arr[i]} '
    sum+=arr[i]
    i+=1
print(res)
print(sum/i)

