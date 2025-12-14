def f(s):
    stack = []
    for x in s.split():
        if x=="+":
            a = float(stack.pop())
            b = float(stack.pop())
            stack.append(a+b)
            continue
        if x=="-":
            a = float(stack.pop())
            b = float(stack.pop())
            stack.append(a-b)
            continue
        if x=="*":
            a = float(stack.pop())
            b = float(stack.pop())
            stack.append(a*b)
            continue
        if x=="/":
            a = float(stack.pop())
            b = float(stack.pop())
            stack.append(a/b)
            continue
        if x=='=':
            return stack.pop()
        else:
            stack.append(float(x))
            



if __name__ == "__main__":
    print(f("8 3 1 + / 3 2 - 4 + * ="))