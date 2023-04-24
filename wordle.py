# Isabel Prado-Tucker
# Menlo School CS1 Final Project
# May 11, 2022
import csv
import random

print('Wordle in the terminal!')
print('You have six tries to guess a 5 letter word.')

# List of possible guesses from Tab Atkins Jr. (@tabatkins) on Github
# https://github.com/tabatkins/wordle-list
words = open('words.txt').read().splitlines()

keys =  ['1', '2', '3', '4', '5']

# List of valid solutions from the The New York Times and Josh Wardle
solutions = open('solutions.txt').read().splitlines()
letter = random.choice(solutions)

def is_word():
    for word in words:
        if guess == word:
            return True
    print('Invalid Guess')
    return False
    
count = 0
guess = ""
guesses = []

def draw_board():
    for g in guesses:
        color = []
        for i in range(len(letter)):
            if g[i] == letter[i]:
                color.append('🟩')
            elif g[i] in letter:
                color.append('🟨')
            else:
                color.append('🟥')
    
        print('--------------------- ------------------------')
        print(f'| {g[0]} | {g[1]} | {g[2]} | {g[3]} | {g[4]} | | {color[0]} | {color[1]} | {color[2]} | {color[3]} | {color[4]} |')
    print('--------------------- ------------------------')


while guess != letter and count < 6:
    guess = input('Guess: ').lower()
    if is_word():
        guesses.append(guess)
        count += 1
    draw_board()

print('The word was ' + letter)
