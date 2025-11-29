def f(name):
    name = name.split()
    result=""
    for x in [x[0] for x in name]:
        result +=x
    return result




if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))