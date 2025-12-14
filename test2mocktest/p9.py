



def f(value):
    count = 0
    with open("data.csv", "r", encoding='UTF-8') as file:
        next(file)  # Skip header
        for line in file:
            fields = line.strip().split(',')
            salary = int(fields[9])  # salary is at index 9
            if salary >= value:
                count += 1
    return count

if __name__ == "__main__":
    print(f(9200))
    print(f(11640))