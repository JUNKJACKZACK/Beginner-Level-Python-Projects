print("Welcome to the basic Python calculator!")
number1 = input("Enter the first number: ")
function = input("Enter your function +-*/: ")
number2 = input("Enter the second number: ")

if function == "+":
    print(int(number1) + int(number2))

elif function == "-":
    print(int(number1) - int(number2))

elif function == "*":
    print(int(number1) * int(number2))

elif function == "/":
    print(int(number1) / int(number2))



    