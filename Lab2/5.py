print("NEVAN KUMAR")
print("22053791")
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def generate_fibonacci_series(length):
    series = [fibonacci(i) for i in range(length)]
    return series
def main():
    try:
        length = int(input("Enter the number of terms for the Fibonacci series: "))
        if length < 0:
            print("Please enter a non-negative integer.")
        else:
            series = generate_fibonacci_series(length)
            print(f"Fibonacci series of {length} terms: {series}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
main()