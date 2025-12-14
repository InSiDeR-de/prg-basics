



def f(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token in ['+', '-']:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            else:
                stack.append(a - b)
        else:
            stack.append(int(token))
    
    return stack[0]

if __name__ == "__main__":
    print(f("2 3 +"))
    print(f("2 6 + 4 5 - +"))
    print(f("11 7 + 15 - 14 +"))