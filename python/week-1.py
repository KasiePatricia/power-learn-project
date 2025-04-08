# Simple Calculator Program
# Performs basic arithmetic operations on two user-provided numbers

def calculator():
    print("\nWelcome to the Simple Calculator!")
    print("Operations available: + (addition), - (subtraction), * (multiplication), / (division)\n")
    
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            print("Invalid operation! Please use +, -, *, or /")
            return
        
        # Display the result
        print(f"\nResult: {num1} {operation} {num2} = {result}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
calculator()