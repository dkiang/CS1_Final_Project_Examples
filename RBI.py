import random  # Imports the random module for generating random numbers.

# This function simulates a baseball at-bat outcome based on player and pitcher statistics.
def simulate_at_bat(batting_avg, on_base_pct, slugging_pct, era):
    weighted_avg = (0.4 * batting_avg) + (0.4 * on_base_pct) + (0.2 * slugging_pct)  # Computes a weighted average from the batting statistics.

    # Determine the potential outcomes of the at-bat based on the comparison of weighted_avg and era.
    if weighted_avg >= era:
        # If the batter's weighted average is equal to or greater than the pitcher's ERA, the batter is more likely to have positive outcomes.
        outcomes = [
            ('single', 0.6),
            ('double', 0.2),
            ('triple', 0.1),
            ('home_run', 0.1),
            ('walk', 0.6),
        ]
    else:
        # If the batter's weighted average is less than the pitcher's ERA, the likelihood of negative outcomes increases.
        outcomes = [
            ('strikeout', 0.4),
            ('ground_out', 0.4),
            ('fly_out', 0.2),
        ]
    
    # Generate a random outcome based on the defined probabilities.
    total_probability = sum([outcome[1] for outcome in outcomes])  # Sums up all probabilities to scale the random choice.
    random_value = random.uniform(0, total_probability)  # Generates a random number within the range of total probability.
    
    cumulative_probability = 0
    for outcome, probability in outcomes:
        cumulative_probability += probability  # Accumulates probabilities to find the interval the random_value falls into.
        if random_value <= cumulative_probability:
            return outcome  # Returns the outcome if the random_value is within the current cumulative probability.

def main():
    # Main function to run the simulation: collects user inputs and displays the result of an at-bat.
    batting_avg = float(input("Enter the batter's batting average (e.g., 0.300): "))  # Input for batter's average.
    on_base_pct = float(input("Enter the batter's on-base percentage (e.g., 0.350): "))  # Input for batter's on-base percentage.
    slugging_pct = float(input("Enter the batter's slugging percentage (e.g., 0.500): "))  # Input for batter's slugging percentage.
    era = float(input("Enter the pitcher's ERA (e.g., 3.00): "))  # Input for pitcher's Earned Run Average (ERA).
    
    result = simulate_at_bat(batting_avg, on_base_pct, slugging_pct, era)  # Calls the simulate_at_bat function with the input stats.
    print(f'The result of the at-bat is: {result}')  # Prints the outcome of the at-bat.

if __name__ == "__main__":
    main()  # Ensures that the main function is called when the script is run as the main module.
