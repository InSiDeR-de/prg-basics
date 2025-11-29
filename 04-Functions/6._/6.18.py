def f(sentence):
    x= sentence.split()
    result = ""
    for y in x:
        result+=f"{y}"
    return result


if __name__ == "__main__":
    print(f("integrated development environment"))
    print(f("a b c"))
    print(f("A programming language is a system of notation for writing computer programs"))