# Import the random module to generate random numbers
import random

# Define a function to generate a math question based on the operator and difficulty level specified
def generate_question(operator, difficulty):
    # If the difficulty level is "easy", generate random single-digit numbers
    if difficulty == "easy":
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    # If the difficulty level is "medium", generate random two-digit numbers
    elif difficulty == "medium":
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    # If the difficulty level is "hard", generate random three-digit numbers
    elif difficulty == "hard":
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)

    # Perform the appropriate mathematical operation on the two numbers based on the specified operator
    if operator == "add":
        return [f"{num1} + {num2} = ", num1 + num2]
    elif operator == "subtract":
        return [f"{num1} - {num2} = ", num1 - num2]
    elif operator == "multiply":
        return [f"{num1} x {num2} = ", num1 * num2]
    elif operator == "divide":
        return [f"{num1} / {num2} = ", num1 / num2]

# Define the main quiz function that generates and presents a series of math problems for the user to solve
def quiz(operator, difficulty):
    # Set the initial score to 0
    score = 0

    # Loop through five iterations to generate five math problems
    for i in range(5):
        # Call the generate_question function to obtain a question and answer pair based on the specified operator and difficulty level
        question, answer = generate_question(operator, difficulty)

        # Prompt the user for an answer and convert it to a float
        user_answer = input(question)
        user_answer = float(user_answer)

        # Compare the user's answer to the correct answer and provide feedback
        if user_answer == answer:
            print("Correct!")
            # If the user's answer is correct, increment the score by 1
            score += 1
        else:
            print(f"Incorrect. The correct answer is {answer}.")

    # Print the user's final score out of five questions
    print(f"You got {score} out of 5 questions correct.")

# If this script is run directly (as opposed to being imported as a module), execute the following code
if __name__ == '__main__':
    # Prompt the user to choose an operator and difficulty level
    operator = input("Choose an operator (add, subtract, multiply, divide): ")
    difficulty = input("Choose a difficulty (easy, medium, hard): ")
    # Call the quiz function with the specified operator and difficulty level
    quiz(operator, difficulty)
