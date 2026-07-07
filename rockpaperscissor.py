import random

choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors Game ===")

user = input("Enter rock, paper, or scissors: ").lower()

computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
elif user in choices:
    print("Computer wins!")
else:
    print("Invalid choice!")