paragraph = "cat dog mouse cat rat cat mouse"
count=0
p = paragraph.split()
y = list(set(p))
for x in y:
    print(x,'in paragraph:', p.count(x))