from math import *
r = int(input())
h = int(input())
l = sqrt(r ** 2 + h ** 2)
V = 1 / 3 * pi * r ** 2 * h
Sbok = pi * r * l
print(f"Образующая = {int(l)}")
print(f"Объем конуса = {int(V)}")
print(f"Площадь боковой поверхности = {int(Sbok)}")