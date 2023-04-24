import random

def simulate_at_bat(batting_avg, on_base_pct, slugging_pct, era):
    weighted_avg = (0.4 * batting_avg) + (0.4 * on_base_pct) + (0.2 * slugging_pct)
    
    if weighted_avg >= era:
        outcomes = [
            ('single', 0.6),
            ('double', 0.2),
            ('triple', 0.1),
            ('home_run', 0.1),
            ('walk', 0.6),
        ]
    else:
        outcomes = [
            ('strikeout', 0.4),
            ('ground_out', 0.4),
            ('fly_out', 0.2),
        ]
    
    total_probability = sum([outcome[1] for outcome in outcomes])
    random_value = random.uniform(0, total_probability)
    
    cumulative_probability = 0
    for outcome, probability in outcomes:
        cumulative_probability += probability
        if random_value <= cumulative_probability:
            return outcome

def main():
    batting_avg = float(input("Enter the batter's batting average (e.g., 0.300): "))
    on_base_pct = float(input("Enter the batter's on-base percentage (e.g., 0.350): "))
    slugging_pct = float(input("Enter the batter's slugging percentage (e.g., 0.500): "))
    era = float(input("Enter the pitcher's ERA (e.g., 3.00): "))
    
    result = simulate_at_bat(batting_avg, on_base_pct, slugging_pct, era)
    print(f'The result of the at-bat is: {result}')

if __name__ == "__main__":
    main()
