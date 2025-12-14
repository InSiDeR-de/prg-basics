###A file report.txt contains an email with shopping report. Write a program that calculates the total value of money spent.
# Calculates the total value of money spent
#
import re # module for regular expressions
result = 0
# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r', encoding="utf-8") as file:
    email=file.read()

# regular expression pattern
# for amounts
pattern = '[0-9]{1,}'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)
# calculate the total purchases
for amount in amounts:
    result+=int(amount)



# print result
print(result)

