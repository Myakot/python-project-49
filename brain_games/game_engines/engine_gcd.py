from brain_games import cli, engine
from math import gcd


def current_correct_answer(a, b):
    correct_answer = str(int(gcd(a, b)))
    print(f'Помощь, чтобы не позориться: correct-answer = {correct_answer}')
    # print(f'DEBUG, correct-answerTYPE = {type(correct_answer)}')
    return correct_answer


def current_case():
    a = engine.get_initial_randomized_number()
    b = engine.get_initial_randomized_number()
    return a, b


def main():
    print('Find the greatest common divisor of given numbers.')
    user_name = cli.welcome_get_name()
    counter = 0
    while counter < 3:
        question = current_case()
        (a, b) = question
        correct_answer = current_correct_answer(a, b)
        print(f'Question: {a} {b}?')
        user_answer = engine.getting_user_answer()
        # print(f'DEBUG, USER-ANSWERTYPE = {type(user_answer)}')
        if correct_answer == user_answer:
            print("Correct!\n")
            counter += 1
        else:
            engine.show_correct_answer(user_answer, correct_answer, user_name)
            return  # Hard reset upon wrong answer

    if counter == 3:
        engine.return_win_end(user_name)



# brain-gcd
#
# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# Find the greatest common divisor of given numbers.
# Question: 25 50
# Your answer: 25
# Correct!
# Question: 100 52
# Your answer: 4
# Correct!
# Question: 3 9
# Your answer: 3
# Correct!
# Congratulations, Sam!