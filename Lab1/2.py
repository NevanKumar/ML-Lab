# Function to check if the number is odd or even
print("NEVAN KUMAR")
print("22053791")
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Input from user
num = int(input("Enter a number: "))

# Calling the function and printing the result
print(check_even_odd(num))
