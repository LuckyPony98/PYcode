import random

def generate_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '+':
        answer = a + b
    elif operator == '-':
        answer = a - b
    elif operator == '*':
        answer = a * b
    else:
        answer = a // b
    question = f"What is {a} {operator} {b}?"
    return question, answer

def main():
    print("Welcome to the basic arithmetic practice program!")
    num_questions = int(input("How many questions would you like to answer? "))
    correct_answers = 0
    for i in range(num_questions):
        question, answer = generate_question()
        user_answer = int(input(question))
        if user_answer == answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Sorry, the correct answer is {answer}")
    print(f"You got {correct_answers} out of {num_questions} questions correct. Good job!")

if __name__ == '__main__':
    main()
