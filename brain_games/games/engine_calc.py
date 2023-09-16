from brain_games import cli, engine
from random import choice


def current_correct_answer(num1, num2, sign):
    if sign == '*':
        correct_answer = str(num1 * num2)
    elif sign == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 + num2)
    return correct_answer


def current_case():
    num1 = engine.get_initial_randomized_number()
    num2 = engine.get_initial_randomized_number()
    sign = choice(['+', '-', '*'])
    return num1, num2, sign


def main():
    print('What is the result of the expression?')
    user_name = cli.welcome_get_name()
    counter = 0
    while counter < 3:
        question = current_case()
        (num1, num2, sign) = question
        correct_answer = current_correct_answer(num1, num2, sign)
        print(f'Question: {num1} {sign} {num2}?')
        user_answer = engine.getting_user_answer()
        if correct_answer == user_answer:
            print("Correct!\n")
            counter += 1
        else:
            engine.show_correct_answer(user_answer, correct_answer, user_name)
            return  # Hard reset upon wrong answer

    if counter == 3:
        engine.return_win_end(user_name)
