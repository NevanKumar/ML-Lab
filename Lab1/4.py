# Input from user
print("NEVAN KUMAR")
print("22053791")
num = int(input("Enter a number: "))

# Check if the number is prime
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a Prime Number")
            break
    else:
        print(f"{num} is a Prime Number")
else:
    print(f"{num} is not a Prime Number")
