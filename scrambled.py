import random

def scramble_word(word):
    scrambled_word = list(word)
    random.shuffle(scrambled_word)
    return ''.join(scrambled_word)

def play_game(words, answers, difficulty):
    index = random.randint(0, len(words) - 1)
    word = words[index]
    answer = answers[index]

    if difficulty == 'easy':
        word = scramble_word(word)
    else:
        word = scramble_word(word[:len(word)//2]) + scramble_word(word[len(word)//2:])
    
    print(f"Scrambled word: {word}")
    user_guess = input("Guess the word: ")

    if user_guess == answer:
        print("Congratulations, you guessed correctly!")
    else:
        print(f"Sorry, the correct answer is {answer}.")

def main():
    words = ["elegant", "freedom", "caliber", "journey", "justice", "sincere", "whistle", "plaster", "require"]
    answers = words.copy()
    difficulty = input("Choose difficulty level (easy or hard): ")

    play_game(words, answers, difficulty)

if __name__ == "__main__":
    main()
