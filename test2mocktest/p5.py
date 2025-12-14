def f(first, last):
    count=0
    with open("data.txt", "r", encoding='UTF-8') as file:
        text = file.read()
        words = text.split()
        for word in words:
            if word[0].lower()==first.lower() and word[-1].lower()==last.lower():
                count+=1
    return count



if __name__ == "__main__":
    print(f("w","d"))