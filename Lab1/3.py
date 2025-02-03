# Input year from user
print("NEVAN KUMAR")
print("22053791")
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
