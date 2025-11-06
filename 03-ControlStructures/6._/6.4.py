###
# Password validator
# New password is at least 12 characters long
#
while True:
    new_password = input('Enter new password: ')
    if len(new_password) < 12:
        print('Password too short (min. 12 chars)')
    else:
       print('Password accepted')
       break