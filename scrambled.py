import random  # Imports the random module for random number generation and shuffling.

def scramble_word(word):
    # Converts the word to a list of characters, shuffles it randomly, and then joins it back into a string.
    scrambled_word = list(word)  # Convert the word into a list of characters.
    random.shuffle(scrambled_word)  # Shuffle the list of characters randomly.
    return ''.join(scrambled_word)  # Join the characters back into a string and return it.

def play_game(words, answers, difficulty):
    # This function plays a word scramble game based on a provided list of words, their answers, and difficulty level.
    index = random.randint(0, len(words) - 1)  # Randomly selects an index for the word to use in the game.
    word = words[index]  # Gets the word at the randomly selected index.
    answer = answers[index]  # Gets the answer for the selected word.

    # Applies different scrambling based on difficulty level.
    if difficulty == 'easy':
        # Scrambles the entire word if the difficulty is 'easy'.
        word = scramble_word(word)
    else:
        # Splits the word into two parts, scrambles them separately, and then combines them if the difficulty is not 'easy'.
        word = scramble_word(word[:len(word)//2]) + scramble_word(word[len(word)//2:])
    
    print(f"Scrambled word: {word}")  # Displays the scrambled word.
    user_guess = input("Guess the word: ")  # Prompts the user to guess the word.

    # Checks if the user's guess is correct and provides feedback.
    if user_guess == answer:
        print("Congratulations, you guessed correctly!")
    else:
        print(f"Sorry, the correct answer is {answer}.")

def main():
    # This function sets up the game by initializing words, copying them as answers, and asking for the difficulty level.
    words = ["elegant", "freedom", "caliber", "journey", "justice", "sincere", "whistle", "plaster", "require"]
    answers = words.copy()  # Makes a copy of the words list to use as answers.
    difficulty = input("Choose difficulty level (easy or hard): ")  # Asks the user to choose a difficulty level.

    play_game(words, answers, difficulty)  # Starts the game with the given settings.

if __name__ == "__main__":
    main()  # Ensures the main function is called when the script is executed directly.
