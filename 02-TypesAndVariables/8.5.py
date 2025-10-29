###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift_code = input("Enter SWIFT code: ")
bank_code = swift_code[0:4]
country_code = swift_code[4:6]
print(f'Bank code: {bank_code}')
print(f'Country code: {country_code}')