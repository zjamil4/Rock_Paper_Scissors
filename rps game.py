import random

options = ("rock", "paper", "scissors")
active = True

while active:
    p1 = None
    computer = random.choice(options)


    while p1 not in options:
            p1 = input("Enter an option (rock, paper or scissors): ")
            print('Player: ' + p1)
            print('Computer: ' + computer)

            if p1 == computer:
                print("It's a tie!")
            elif p1 == "paper" and computer == "rock":
                print("You win!")
            elif p1 == "rock" and computer == "scissors":
                print("You win!")
            elif p1 == "scissors" and computer == "paper":
                print("You win!")
            else:
                print("You lose! :(")

            retry = input("Would you like to play again? (yes/no): ").lower()
            if not retry == "yes":
                active = False

print("Thanks for playing!")