from random import choice, randint
from brain_games.constants import DESC_CALC


def create_question_answer():
    number1 = randint(-100, 100)
    number2 = randint(-100, 100)
    sign = choice(['+', '-', '*'])
    question = f'{number1} {sign} {number2}'

    if sign == '*':
        correct_answer = str(number1 * number2)
    elif sign == '-':
        correct_answer = str(number1 - number2)
    else:
        correct_answer = str(number1 + number2)
    return correct_answer, question


def print_game_desc():
    desc = DESC_CALC
    print(desc)
