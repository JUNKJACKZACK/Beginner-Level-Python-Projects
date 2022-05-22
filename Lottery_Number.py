
from ast import Break
import random


print("Welcome to the Lottery Number Generator")

age = input("Enter you age to play: ")

if int(age) < 18:
    print("Sorry you are not of legal age")
    
else:
    print(random.randint(0,99))
    print(random.randint(0,99))
    print(random.randint(0,99))
    print(random.randint(0,99))
    print(random.randint(0,99))
    print(random.randint(0,99))
    
Break
