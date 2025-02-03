print("NEVAN KUMAR")
print("22053791")
# Create a dictionary with initial key-value pairs
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Function to display the menu
def display_menu():
    print("\nSelect an operation:")
    print("1. View value by key")
    print("2. Add a new key-value pair")
    print("3. Update an existing key-value pair")
    print("4. Remove a key-value pair")
    print("5. Check if a key exists")
    print("6. Display all key-value pairs")
    print("7. Exit")

# Function to view value by key
def view_value():
    key = input("Enter the key to view: ")
    if key in my_dict:
        print(f"Value for '{key}': {my_dict[key]}")
    else:
        print(f"Key '{key}' not found.")

# Function to add a new key-value pair
def add_value():
    key = input("Enter the key to add: ")
    value = input(f"Enter the value for '{key}': ")
    my_dict[key] = value
    print(f"Added '{key}': {value}")

# Function to update an existing key-value pair
def update_value():
    key = input("Enter the key to update: ")
    if key in my_dict:
        value = input(f"Enter the new value for '{key}': ")
        my_dict[key] = value
        print(f"Updated '{key}' to '{value}'")
    else:
        print(f"Key '{key}' not found.")

# Function to remove a key-value pair
def remove_value():
    key = input("Enter the key to remove: ")
    if key in my_dict:
        my_dict.pop(key)
        print(f"Removed key '{key}'")
    else:
        print(f"Key '{key}' not found.")

# Function to check if a key exists
def check_key():
    key = input("Enter the key to check: ")
    if key in my_dict:
        print(f"Key '{key}' exists.")
    else:
        print(f"Key '{key}' does not exist.")

# Function to display all key-value pairs
def display_all():
    if my_dict:
        print("\nAll key-value pairs:")
        for key, value in my_dict.items():
            print(f"{key}: {value}")
    else:
        print("The dictionary is empty.")

# Main program loop
while True:
    display_menu()
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        view_value()
    elif choice == '2':
        add_value()
    elif choice == '3':
        update_value()
    elif choice == '4':
        remove_value()
    elif choice == '5':
        check_key()
    elif choice == '6':
        display_all()
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")