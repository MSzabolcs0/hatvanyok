import random

options = ("rock", "paper", "scissors")
running = True

while running:
    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Enter rock, paper or scissors: ").lower()

    print(f"Your choice: {player}")
    print(f"Computer's choice: {computer}")

    if player == computer:
        print("It's a tie!")

    elif player == "rock" and computer == "scissors" or player == "scissors" and computer == "paper" or player == "paper" and computer == "rock":
        print("You won!")

    else:
        print("You lost!")

    if not input("Do you want to play again? (y/n)").lower == "y":
        running = False



print("Thanks for playing!")