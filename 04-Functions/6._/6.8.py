def f(amount_to_pay):
    result=0
    while amount_to_pay>0:
        if amount_to_pay >=5:
            result += amount_to_pay//5
            amount_to_pay = amount_to_pay%5
            continue
        elif amount_to_pay >= 2:
            result += amount_to_pay//2
            amount_to_pay = amount_to_pay%2
            continue
        else:
            result += amount_to_pay//1
            amount_to_pay = amount_to_pay%1
            
    return result
        




if __name__ == "__main__":
    print(f(23))
    print(f(8))
    print(f(2))