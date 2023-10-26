import random
from brain_games.consts import GAME_GREET_CALC
from brain_games.utils import get_random_num
from brain_games.engine import run_game


def get_random_math_sign_and_result(number1, number2):
    sign = random.choice(['+', '-', '*'])
    question = f'{number1} {sign} {number2}'
    match sign:
        case '*':
            correct_answer = number1 * number2
        case '-':
            correct_answer = number1 - number2
        case '+':
            correct_answer = number1 + number2
    return correct_answer, question


def get_math_question_and_result():
    number1, number2 = get_random_num(), get_random_num()
    correct_answer, question = get_random_math_sign_and_result(number1, number2)
    return str(correct_answer), question


def run_calc_game():
    run_game(GAME_GREET_CALC, get_math_question_and_result)
