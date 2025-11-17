i=int(input("Enter the ammount in PLN: "))

print(f"5 PLN coins: {i//5}")
i=i%5
print(f"2 PLN coins: {i//2}")
i=i%2
print(f"1 PLN coins: {i//1}")
i=1%1


