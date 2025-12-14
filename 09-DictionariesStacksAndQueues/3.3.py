import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    bracket_stack = queue.LifoQueue()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            bracket_stack.put(char)
        elif char in closing_brackets:
            if bracket_stack.empty():
                return False
            top_bracket = bracket_stack.get()
            if matching_brackets[char] != top_bracket:
                return False

    if bracket_stack.empty():
        return True
    else:
        return False

if brackets_ok(expression1):
   print("Brackets in expression1 are correct.")
else:
    print("Brackets in expression1 are NOT correct.")

if brackets_ok(expression2):
    print("Brackets in expression2 are correct.")
else:
    print("Brackets in expression2 are NOT correct.")

if brackets_ok(expression3):
    print("Brackets in expression3 are correct.")
else:
    print("Brackets in expression3 are NOT correct.")