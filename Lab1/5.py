# Initialize an empty list
print("NEVAN KUMAR")
print("22053791")
numbers = []

# Input 10 numbers from the user
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Print the list in reverse order
print("The numbers in reverse order are:")
print(numbers[::-1])
