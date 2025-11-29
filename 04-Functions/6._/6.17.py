def f(palindrome):
    n=1
    for x in palindrome:
        if x == palindrome[len(palindrome)-n]:
            n+=1
            result = True
            continue
        else:
            result = False
            break
    return result




if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))