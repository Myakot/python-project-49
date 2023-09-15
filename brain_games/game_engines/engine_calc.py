from brain_games import cli, engine
from random import choice


def current_correct_answer(question):
    (a, b, sign) = question
    if sign == '*':
        correct_answer = str(a * b)
    elif sign == '-':
        correct_answer = str(a - b)
    else:
        correct_answer = str(a + b)
    return correct_answer


def current_case():
    a = engine.get_initial_randomized_number()
    b = engine.get_initial_randomized_number()
    sign = choice(['+', '-', '*'])
    return a, b, sign


def main():
    print('What is the result of the expression?')
    user_name = cli.welcome_get_name()
    counter = 0
    while counter < 3:
        question = current_case()
        correct_answer = current_correct_answer(question)
        (a, b, sign) = question
        # Куратору - Хочу поменять это ^^^, я в двух местах распаковываю tuple
        print(f'Question: {a} {sign} {b}?')
        user_answer = engine.getting_user_answer()
        if correct_answer == user_answer:
            print("Correct!\n")
            counter += 1
        else:
            engine.show_correct_answer(user_answer, correct_answer, user_name)
            return  # Hard reset upon wrong answer

    if counter == 3:
        engine.return_win_end(user_name)
