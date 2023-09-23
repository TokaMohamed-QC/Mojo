#conditions
name = input("Enter your name: ")
if (name == "Toka"):
    print("Hello {}".format(name))
elif name == "Aliaa":
    print("Hello {}".format(name))
    
print("Have a nice day!")

#calacualtor function

on = True

def add():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print (a+b)

def subtract():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print (a-b)

def Multiply():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print (a*b)

def divide():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print (a/b)

while on:

    operation = input ("Enter operation: +, -, *, /: ")

    if operation == "+":
       add()
    elif operation == "-":
       subtract()
    elif operation == "*":
       Multiply()
    elif operation == "/":
       divide()
    elif operation == "q":
        on = False
    else: print("This is not valid operation")