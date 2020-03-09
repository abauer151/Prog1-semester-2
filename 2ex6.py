# Aidan Bauer 3/5/20
from turtle import *
numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter denominator: "))

# If denominator is 0, this will result in a division-
# by-zero error! Add in code to solve this issue:
try:
    x = numerator / denominator
    if numerator / denominator * denominator == numerator:
        print("Divides evenly!")
    else:
        print("Doesn't divide evenly.")
except ZeroDivisionError:
    print("Can't divide by zero")