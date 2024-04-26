import random

def main():
    favorite_restaurants = get_favorite_restaurants()
    print("Your favorite restaurants are:", favorite_restaurants)

    while True:
        user_input = input("Type 'recommend' to get a recommendation or 'quit' to exit the program: ").lower()
        if user_input == 'recommend':
            recommend_restaurant(favorite_restaurants)
        elif user_input == 'quit':
            break
        else:
            print("Invalid input. Please try again.")

def get_favorite_restaurants():
    restaurants = []
    while True:
        restaurant_name = input("Enter the name of one of your favorite restaurants (or type 'done' to finish): ")
        if restaurant_name.lower() == 'done':
            break
        rating = int(input("Rate this restaurant from 1 to 5: "))
        while rating < 1 or rating > 5:
            print("Invalid rating. Please enter a rating from 1 to 5.")
            rating = int(input("Rate this restaurant from 1 to 5: "))
        restaurants.append((restaurant_name, rating))
    return restaurants

def recommend_restaurant(restaurants):
    if not restaurants:
        print("You haven't added any restaurants to the list.")
    else:
        # Create a list of choices weighted by the rating
        weighted_choices = [restaurant for restaurant, rating in restaurants for _ in range(rating)]
        choice = random.choice(weighted_choices)
        print(f"We recommend you visit {choice}.")

if __name__ == "__main__":
    main()
