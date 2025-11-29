
def fibonacci_sequence(n):
    sequence = []
    a= 0
    b = 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    print(f"The first twenty words of the Fibonacci sequence are: {fibonacci_sequence(20)}")

    