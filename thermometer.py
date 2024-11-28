def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

def main():
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}! Welcome to the Temperature Conversion Program.")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is {celsius:.2f} Celsius")
    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is {fahrenheit:.2f} Fahrenheit")
    else:
        print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
