import random

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    computer_choice = random.randint(0, 2)
    choices = ["Rock", "Paper", "Scissors"]
    print(f"Computer chose: {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You Win!")
    else:
        print("You Lose!")
