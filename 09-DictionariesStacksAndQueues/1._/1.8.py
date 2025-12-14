price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
total=0
total1=0
print("Product;   Price")
for x in price_list.items():
    print(f'{x[0]}   {x[1]}')
    total+=x[1]
print(f'Total; {round(total,2)}')
print('After;')
for x in price_list.items():
    print(f'{x[0]}   {x[1]*0.9}')
    total1+=x[1]
print(f'Total; {round(total1,2)}')

