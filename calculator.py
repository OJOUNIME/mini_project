def add(num1, num2):
    return(num1 + num2)
def subtract(num1, num2):
    return(num1 - num2)
def multiply(num1, num2):
    return(num1 * num2)
def divide(num1, num2):
    return(num1 / num2)

num1 = float(input("enter first number: "))
op = input("enter operators(+, -, *, /): ")
num2 = float(input("enter second number: "))
if op == "+":
    print("result:", add(num1, num2) )
elif op == "-":
    print("results:", subtract(num1, num2))
elif op == "*":
    print("results:", multiply(num1, num2))
elif op == "/":
    print("results;", divide(num1, num2))
    if num2 == 0:
         print("error: cannot divide by zero")
else: print("unkown operator")