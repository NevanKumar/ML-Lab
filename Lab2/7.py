print("NEVAN KUMAR")
print("22053791")
def is_palindrome(number):
    return str(number) == str(number)[::-1]

def is_perfect(number):
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number

def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == number

def main():
    try:
        num = int(input("Enter a number: "))
        if is_palindrome(num):
            print(f"{num} is a Palindrome number.")
        else:
            print(f"{num} is not a Palindrome number.")
            
        if is_perfect(num):
            print(f"{num} is a Perfect number.")
        else:
            print(f"{num} is not a Perfect number.")
            
        if is_armstrong(num):
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")
main()