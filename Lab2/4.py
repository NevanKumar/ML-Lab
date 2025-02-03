print("NEVAN KUMAR")
print("22053791")
def decimal_to_binary(decimal_num):
        return bin(decimal_num)[2:] 
def binary_to_decimal(binary_num):
        return int(binary_num, 2)  
def main():
    print("Number Conversion Program")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        try:
            decimal_num = int(input("Enter a decimal number: "))
            binary_result = decimal_to_binary(decimal_num)
            print(f"The binary representation of {decimal_num} is: {binary_result}")
        except ValueError:
            print("Invalid input! Please enter a valid decimal number.")
    elif choice == '2':
        binary_num = input("Enter a binary number: ")
        if all(char in '01' for char in binary_num): 
            decimal_result = binary_to_decimal(binary_num)
            print(f"The decimal representation of {binary_num} is: {decimal_result}")
        else:
            print("Invalid input! Please enter a valid binary number (only 0s and 1s).")
    else:
        print("Invalid choice! Please select 1 or 2.")
main()