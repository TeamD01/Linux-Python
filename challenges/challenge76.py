#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes.

Modified to inclued:

    Take a mulligan (re-roll if total dice sum is less than 9. What a bad sport!)
    Rolls one additional die.
    Weighted dice (the first die is weighted so it can't roll below a three)
    SABOTAGE (one player has replaced the other player's dice with die that won't roll above a 3!)"""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Cheat_Mulligan
from cheatdice import Cheat_Extra_Die
from cheatdice import Cheat_Lucky_Die
from cheatdice import Cheat_Saboteur

def main():
    """run-time code"""

    # create two cheater objects
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6
    #cheater1 = Cheat_Mulligan() # if total < 9 get a re-roll
    #cheater2 = Cheat_Extra_Die() # roll an additional die
    #cheater1 = Cheat_Lucky_Die() # first die is luck and can't roll <3
    #cheater2 = Cheat_Saboteur() # switch player's dice with dice that can't roll > 6


    # both players take turns
    cheater1.roll()
    cheater2.roll()

    # both players use their cheat methods
    cheater1.cheat()
    cheater2.cheat()


    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 1 wins!")

    else:
        print("Cheater 2 wins!")

if __name__ == "__main__":
    main()

