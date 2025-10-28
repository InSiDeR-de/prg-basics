###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Dawid'   # replace Anna with your name
surname = 'Piechura' # replace May with your surname
characters_in_name = len(name)
characters_in_surname = len(surname)
full_name = name + ' ' + surname
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {len(full_name)} characters with aspace between name and surname')  # with aspace between name and surname