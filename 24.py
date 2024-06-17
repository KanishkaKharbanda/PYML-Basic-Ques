def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
    
while True:
    print("Simple Calculator")
    print("Enter 'q' to quit")
        
    num1 = input("Enter the first number: ")
    if num1.lower() == 'q':
        break
    num2 = input("Enter the second number: ")
    if num2.lower() == 'q':
        break
        
    operator = input("Enter an operator (+, -, *, /): ")
    if operator.lower() == 'q':
        break
        
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue
        
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operator. Please enter one of +, -, *, /.")
        continue
        
    print(f"The result is: {result}\n")
