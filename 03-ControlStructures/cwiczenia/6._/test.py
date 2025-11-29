#(p3.py) A text contains any number of words. Define a function f(name) that returns the acronym (the first letters of all words). Sample result:
#f("Internet of Things") returns "IoT"

def acronym(name):
    words = name.split()
    acronym_letters = [word[0] for word in words]
    return ''.join(acronym_letters)
