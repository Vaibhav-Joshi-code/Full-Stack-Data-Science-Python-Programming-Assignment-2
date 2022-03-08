# 4.Write a Python program to solve quadratic equation
a = eval(input("Enter second degree coefficient: "))
b = eval(input("Enter linear term coefficient: "))
c = eval(input("Enter constant term"))
import math
from math import sqrt

if (b**2 - (4*a*c))>=0:
    D = sqrt(b**2 - (4*a*c))
    root1 = (-b + sqrt(D))/2*a
    root2 = (-b - sqrt(D))/2*a
    print(f"The quadratic equation is: {a}x^2 + {b}x + c = 0")
    print(f"The roots of this quadratic equation are: {root1} and {root2}")
else:
    print("No real roots")

