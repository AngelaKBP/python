def calculator():
    guest_name = input("Enter your name: ")
    print(f"Hello, {guest_name}! Welcome to the simple calculator.")
    
    print("You will need an operator:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error! Division by zero."
        else:
            return "Invalid operator!"

        return f"The result is: {result}"
    except ValueError:
        return "Invalid input! Please enter numeric values."

if __name__ == "__main__":
    print(calculator())