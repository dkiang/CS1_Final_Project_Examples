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
        user_input = input("Enter the name of one of your favorite restaurants (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        else:
            restaurants.append(user_input)
    return restaurants

def recommend_restaurant(restaurants):
    if not restaurants:
        print("You haven't added any restaurants to the list.")
    else:
        choice = random.choice(restaurants)
        print(f"We recommend you visit {choice}.")

if __name__ == "__main__":
    main()
