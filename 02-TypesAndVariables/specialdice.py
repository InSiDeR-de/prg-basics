import random
roll=random.randint(1, 6)
valid= roll == 1 or roll == 6
print('Die roll: ', roll)
print('Is the roll special (1 or 6): ', valid)