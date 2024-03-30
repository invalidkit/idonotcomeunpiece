import random

x = 0

one = random.randint(0, 3)
a = int(input('First number: '))
b = int(input('Second number: '))

if one == 0:
    x = a+b
elif one == 1:
    x = a-b
elif one == 2:
    x = a*b
elif one == 3:
    x = a/b

print(x)