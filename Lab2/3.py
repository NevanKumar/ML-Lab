import random
print("NEVAN KUMAR")
print("22053791")

def set_weight_game():
    print("Welcome to the 'Set Weight' game!")
    print("Rules:")
    print("1. The total weight starts at 0 and must reach exactly 50.")
    print("2. Players alternately choose a unique weight between 1 and 9.")
    print("3. The player who gives the last weight to reach 50 wins.")
    print("\nLet's start!\n")
    
    total_weight = 0
    used_weights = set()
    
    while total_weight < 50:
        # User's turn
        try:
            user_weight = int(input(f"Total weight is {total_weight}. Enter your weight (1-9): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue
        
        # Validate user input
        if user_weight < 1 or user_weight > 9:
            print("Invalid weight! Please choose a number between 1 and 9.")
            continue
        if user_weight in used_weights:
            print("This weight has already been used. Choose another weight.")
            continue

        # Update total and used weights
        total_weight += user_weight
        used_weights.add(user_weight)
        
        if total_weight == 50:
            print(f"Total weight is now {total_weight}. Congratulations! You win!")
            break
        elif total_weight > 50:
            print(f"Total weight is now {total_weight}. You've exceeded 50. You lose!")
            break
        
        # Computer's turn
        available_weights = [w for w in range(1, 10) if w not in used_weights]
        computer_weight = random.choice(available_weights)
        print(f"Computer chooses: {computer_weight}")
        
        # Update total and used weights
        total_weight += computer_weight
        used_weights.add(computer_weight)
        
        if total_weight == 50:
            print(f"Total weight is now {total_weight}. Computer wins!")
            break
        elif total_weight > 50:
            print(f"Total weight is now {total_weight}. Computer loses! You win!")
            break
set_weight_game()