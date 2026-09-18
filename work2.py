#simple calculator
#define the maths operators using functions.
def add(num1, num2):
    return(num1 + num2)
def subtract(num1, num2):
    return(num1 - num2)
def multiply(num1, num2):
    return(num1 * num2)
def divide(num1, num2):
    return(num1 / num2)
# take user input
num1 = float(input("enter first number: "))
op = input("enter operators(+, -, *, /): ")
num2 = float(input("enter second number: "))
# use the if, elif and else to choose the right function
if op == "+":
    print("results:", add(num1, num2))
elif op == "-":
    print("results:", subtract(num1, num2))
elif op == "*":
    print("results:", multiply(num1, num2))
elif op == "/":
    
    if num2 == 0:
        print("error: cannot divide by zero")
    else:
        print("results:", divide(num1, num2))
        
else:
    print("unknown operators")


    