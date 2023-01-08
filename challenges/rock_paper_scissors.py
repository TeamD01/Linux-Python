# ROCK, PAPER, SCISSORS...

# for random computer choice
import random

def main():
    start = True
    while start:  #for play again decisions
        # Player choice
        print("\nPlease enter your input: 1: Rock 2. Paper 3: Scissors")
        player = int(input("Your choice: "))

        # computer choice
        # random number between 1 and 3
        computer = random.randint(1, 3)

        # dictionary keys: 1,2,3 to values: rock, paper, scissors
        choice = {1: "Rock", 2: "Paper", 3: "Scissors"}
        print(f"Player: {choice[player]} Computer: {choice[computer]}")

        # who won?
        if(player == computer):
            print("It's Draw!")
        elif (player == 1 and computer == 2):
            print("Paper covers Rock. Computer wins! ")
        elif (player == 1 and computer == 3):
            print("Rock smashes Scissors. You win! \U0001F600")
        elif (player == 2 and computer == 1):
            print("Paper covers Rock. You win! \U0001F600")
        elif (player == 2 and computer == 3):
            print("Scissors cuts Paper. Computer wins! ")
        elif (player == 3 and computer == 1):
            print("Rock smashes Scissors. Computer wins! ")
        elif (player == 3 and computer == 2):
            print("Scissors cuts Paper. You win! \U0001F600")

        # Play again?
        print("\nDo you want to play again? (y/n)")
        if(input() == "n"):
            start = False
            print("Game over!")
        else:
            continue
if __name__ == "__main__":
    main()
