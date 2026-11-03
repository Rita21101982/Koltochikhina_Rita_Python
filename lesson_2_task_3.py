# Площадь квадрата

import math


def square(x):
    s = x * x
    return math.ceil (s)

x = float(input("Введите длину стороны квадрата: "))

result = (square(x))

print(f"Площадь квадрата = {result}")

