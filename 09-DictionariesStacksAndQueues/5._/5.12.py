stack=[]
word=input("Enter a word: ")
for letter in word:
    stack.append(letter)
print(word)
i=0
while i<len(stack):
    z = stack.pop()
    print(f'{z}',end='')