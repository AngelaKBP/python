# A program that evaluates a user's mathematical expression and returns the order of operations that were performed

def explain_precedence(expression):
    precedence = {
        '**': 'Exponentiation',
        '*': 'Multiplication',
        '/': 'Division',
        '//': 'Floor Division',
        '%': 'Modulus',
        '+': 'Addition',
        '-': 'Subtraction'
    }
# Explanation of the order of operations     
    explanation = []
    for operator in precedence:
        if operator in expression:
            explanation.append(f"{operator}: {precedence[operator]}")
  
    return explanation

def main():
    name = input("Enter your name: ")
    while True:
        expression = input(f"{name}, enter a mathematical expression: ")
        try:
# Result of the expression
            result = eval(expression)
            print(f"The result of the expression '{expression}' is: {result}")
            
            explanation = explain_precedence(expression)
            print("\nOrder of Operation:")
            for line in explanation:
                print(line)
        except Exception as e:
            print(f"Error evaluating expression: {e}")
# Allow user to evaluate another expression        
        another = input("Would you like to evaluate another expression? (yes/no): ").strip().lower()
        if another != 'yes':
            print(f"Goodbye, {name}!")
            break

if __name__ == "__main__":
    main()