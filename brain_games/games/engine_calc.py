from brain_games.engine import get_initial_randomized_number
from brain_games.engine import welcome_get_name
from brain_games.engine import getting_user_answer
from brain_games.engine import show_correct_answer
from brain_games.engine import return_win_end
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
    num1 = get_initial_randomized_number()
    num2 = get_initial_randomized_number()
    sign = choice(['+', '-', '*'])
    return num1, num2, sign


def main():
    print('What is the result of the expression?')
    user_name = welcome_get_name()
    counter = 0
    while counter < 3:
        question = current_case()
        (num1, num2, sign) = question
        correct_answer = current_correct_answer(num1, num2, sign)
        print(f'Question: {num1} {sign} {num2}')
        user_answer = getting_user_answer()
        if correct_answer == user_answer:
            print("Correct!\n")
            counter += 1
        else:
            show_correct_answer(user_answer, correct_answer, user_name)
            return

    if counter == 3:
        return_win_end(user_name)
