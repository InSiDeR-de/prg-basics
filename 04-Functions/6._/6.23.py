#A valid password should consist of at least six characters and each character appears only once in the password. Define a function f(password) that returns True if the password is correct or False otherwise. Sample result:

#f("ax15") returns False
#f("book123") returns False
#f("A2water3") returns True



def f(password):
    if len(password) < 6:
        return False
    for char in password:
        if password.count(char) > 1:
            return False
    return True



if __name__ == "__main__":
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))