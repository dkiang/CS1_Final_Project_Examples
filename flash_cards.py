import random

def generate_question(operator, difficulty):
    if difficulty == "easy":
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif difficulty == "medium":
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    elif difficulty == "hard":
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)

    if operator == "add":
        return f"{num1} + {num2} = ", num1 + num2
    elif operator == "subtract":
        return f"{num1} - {num2} = ", num1 - num2
    elif operator == "multiply":
        return f"{num1} x {num2} = ", num1 * num2
    elif operator == "divide":
        return f"{num1} / {num2} = ", num1 / num2

def quiz(operator, difficulty):
    score = 0
    for i in range(5):
        question, answer = generate_question(operator, difficulty)
        user_answer = input(question)
        if float(user_answer) == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {answer}.")
    print(f"You got {score} out of 5 questions correct.")

if __name__ == '__main__':
    operator = input("Choose an operator (add, subtract, multiply, divide): ")
    difficulty = input("Choose a difficulty (easy, medium, hard): ")
    quiz(operator, difficulty)
