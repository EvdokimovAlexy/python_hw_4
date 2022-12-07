import math
d = int(input("введите точность числа пи: "))
pi = math.pi
x = str(pi)
print(f'{pi}\n{x[0:d+2:1]}')