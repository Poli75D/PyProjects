import string
import random

def f_PassGen():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for x in range(0, l))

def f_checker(val):
    if val.isnumeric():
        val = int(val)
    else:
        val = 0
    return val

n = 0
while n == 0:
    n = input('How many passwords?: ')
    n = f_checker(n)
    if n == 0:
        print('Please, give me a number at least 1')

l = 0
while l == 0:
    l = input('How long passwords?: ')
    l = f_checker(l)
    if l == 0:
        print('Please, give me a number at least 1')

i = 0
while i < n:
    print(f_PassGen())
    i += 1
