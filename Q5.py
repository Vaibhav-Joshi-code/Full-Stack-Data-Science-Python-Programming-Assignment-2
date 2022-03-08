# Write a Python Program to swap two variables without temp variable
a = eval(input("Enter value for a: "))
b = eval(input("Enter value for b: "))
print("Before swap: ")
print(f"a = {a}, b = {b}")

a,b = b,a
print("After swap: ")
print(f"a = {a}, b={b}")
