from random import choice
from brain_games.consts import DESC_CALC
from brain_games.utils import random_num


def create_question_answer():
    number1 = random_num()
    number2 = random_num()
    sign = choice(['+', '-', '*'])
    question = f'{number1} {sign} {number2}'
    correct_answer = check_for_answer(number1, sign, number2)
    return correct_answer, question


def check_for_answer(number1, sign, number2):
    if sign == '*':
        correct_answer = str(number1 * number2)
    elif sign == '-':
        correct_answer = str(number1 - number2)
    else:
        correct_answer = str(number1 + number2)
    return correct_answer


def print_game_desc():
    desc = DESC_CALC
    print(desc)
