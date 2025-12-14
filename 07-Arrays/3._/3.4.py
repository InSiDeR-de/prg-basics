arr= [-15, 8, -31, 47, -2, 19]
max_num=0
min_num=0
for x in arr:
    if x>max_num:
        max_num=x
    else:
        continue
for y in arr:
    if y<min_num:
        min_num=y
    else:
        continue
print(min_num)
print(max_num)