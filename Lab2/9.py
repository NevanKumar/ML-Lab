print("NEVAN KUMAR")
print("22053791")
def main():
    # Create an empty list
    numbers = []

    while True:
        print("\nList Operations Menu:")
        print("1. Add an element")
        print("2. Remove an element")
        print("3. Access an element by index")
        print("4. Display the list")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                # Add an element
                element = int(input("Enter a number to add: "))
                numbers.append(element)
                print(f"{element} has been added to the list.")
            
            elif choice == 2:
                # Remove an element
                if not numbers:
                    print("The list is empty. Nothing to remove.")
                else:
                    element = int(input("Enter the number to remove: "))
                    if element in numbers:
                        numbers.remove(element)
                        print(f"{element} has been removed from the list.")
                    else:
                        print(f"{element} is not in the list.")
            
            elif choice == 3:
                # Access an element by index
                if not numbers:
                    print("The list is empty.")
                else:
                    index = int(input(f"Enter an index (0 to {len(numbers) - 1}): "))
                    if 0 <= index < len(numbers):
                        print(f"The element at index {index} is {numbers[index]}.")
                    else:
                        print("Invalid index.")
            
            elif choice == 4:
                # Display the list
                print(f"The current list is: {numbers}")
            
            elif choice == 5:
                # Exit
                print("Exiting the program. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select from the menu.")
        
        except ValueError:
            print("Invalid input! Please enter a number.")
main()