 #Define the function f(n) that returns the n-th prime number. A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:

#f(1) returns 2
#f(5) returns 11
def f(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1
    return num



if __name__ == "__main__":
    print(f(1))
    print(f(5))
    print(f(20))