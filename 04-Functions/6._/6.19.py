#Define a function f(number) that returns the sum of repeated digits in a number. Sample result: 
# f(1027) returns 0
#f(230335) returns 9
#f(513553007) returns 21

def f(number):
    num_str = str(number)
    digit_count = {}
    for digit in num_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    result = 0
    for digit, count in digit_count.items():
        if count > 1:
            result += int(digit) * count

    return result

    
if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))
    print(f(221))