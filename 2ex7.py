#Aidan Bauer 3/5/20
from turtle import*
def retrieve_positive_number():
    try:
        num = int(input("Enter a positive number"))
    except:
        print("Try again, it is not positive")
retrieve_positive_number()