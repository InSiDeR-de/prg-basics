r=5

for i in range(r+1):
    for x in range(i):
        print("*",end="")
    print()
for i in reversed(range(r)):
    for x in range(i):
        print("*",end="")
    print()
