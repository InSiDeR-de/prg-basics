###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[len(arr)-1])
print('Last but one value', arr[len(arr)-2])
print('sum of the first and last value', arr[0]+arr[len(arr)-1])
print('Second value', arr[len(arr)//2])
for x in arr:
    print(f"{x} ", end="")

...