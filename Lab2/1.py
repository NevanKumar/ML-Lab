print("NEVAN KUMAR")
print("22053791")
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."
def main():
    print("Choose an operation to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")    
    choice = input("Enter your choice (1/2/3/4): ")
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        return
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    if choice == '1':
        print(f"The result of addition is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result of subtraction is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result of multiplication is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result of division is: {divide(num1, num2)}")
main()