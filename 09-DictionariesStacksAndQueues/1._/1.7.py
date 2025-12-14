product_inventory = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
total=0
for product in product_inventory.items():
    print(f"Product: {product[0]}, Quantity in Stock: {product[1]}")
    total+=product[1]
print('---')
print(f"Total products: {total}")
