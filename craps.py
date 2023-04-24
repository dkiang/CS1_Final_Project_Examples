import random

# Define a function to roll two dice and return their sum
def roll_dice():
    """
    Rolls two dice and returns their sum.
    """
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

# Define the main function that plays the game of craps
def main():
    """
    Plays the game of craps.
    """
    # Initialize the game state
    bankroll = 1000  # Starting bankroll
    point = None  # Current point value

    # Loop until the player runs out of money or chooses to quit
    while bankroll > 0:
        print(f"Bankroll: ${bankroll}")

        # Get the player's bet
        bet = int(input("Enter your bet: "))
        if bet > bankroll:
            print("You don't have enough money for that bet.")
            continue

        # Roll the dice and print the result
        roll = roll_dice()
        print(f"You rolled {roll}.")

        # Determine the outcome of the roll
        if point is None:
            # If the player hasn't established a point yet
            if roll in [7, 11]:
                print("You win!")
                bankroll += bet
            elif roll in [2, 3, 12]:
                print("You lose!")
                bankroll -= bet
            else:
                point = roll
                print(f"Point is {point}.")
        else:
            # If the player has established a point
            if roll == point:
                print("You win!")
                bankroll += bet
                point = None
            elif roll == 7:
                print("You lose!")
                bankroll -= bet
                point = None
            else:
                print(f"Roll again. Point is {point}.")

        # Check if the game is over
        if bankroll == 0:
            print("Game over. You're out of money.")
        else:
            play_again = input("Play again? (y/n)").lower()
            if play_again == 'n':
                print("Thanks for playing!")
                break

# Start the game of craps
main()
