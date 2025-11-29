#The sequence of digits contains the number of points rolled with a dice. Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row. Sample result:

#f("5233165554211") returns 5
#f("2133") returns 3
#f("213311") returns 1


def f(dice):
    if not dice:
        return None
    max_len = 0
    max_digit = None
    cur_len = 0
    prev = None
    for ch in dice:
        if ch == prev:
            cur_len += 1
        else:
            cur_len = 1
            prev = ch
        if cur_len > max_len:
            max_len = cur_len
            max_digit = ch
        elif cur_len == max_len:
            if max_digit is None or int(ch) < int(max_digit):
                max_digit = ch
    return int(max_digit)

if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))
    print(f("213311"))
