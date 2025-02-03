# Function to check if a number is prime
print("NEVAN KUMAR")
print("22053791")
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False

# Input 10 numbers into a list
numbers = [int(input("Enter a number: ")) for _ in range(10)]

# Print all prime numbers from the list
print("Prime numbers in the list:")
for num in numbers:
    if is_prime(num):
        print(num)
