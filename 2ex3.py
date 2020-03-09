#Aidan Bauer 3/3/20
from turtle import *
num1 = int(input("What is the 1st number"))
num2 = int(input("What is the 2nd number"))
operation = input("What is the operation")
if operation == "addition":
    total = num1 + num2
    print(total)

if operation == "subtraction":
    total = num1 - num2
    print(total)

if operation == "multiplication":
    total = num1 * num2
    print(total)

if operation == "division":
    total = num1 / num2
    print(total)
