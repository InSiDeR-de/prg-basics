amount_str = input('Amount: ')
amount = round(float(amount_str),2)
vat = round(amount * 0.23, 2)
print(f'VAT on Amount {amount} is {vat}')