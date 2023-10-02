from random import choice
from brain_games.consts import GAME_GREET_CALC
from brain_games.utils import get_random_num
from brain_games.engine import engine_game_start


def give_question_and_answer():
    number1, number2 = get_random_num(), get_random_num()
    sign = choice(['+', '-', '*'])
    question = f'{number1} {sign} {number2}'
    correct_answer = check_for_answer(number1, sign, number2)
    return correct_answer, question


def check_for_answer(number1, sign, number2):
    match sign:
        case '*':
            correct_answer = str(number1 * number2)
        case '-':
            correct_answer = str(number1 - number2)
        case '+':
            correct_answer = str(number1 + number2)
    return correct_answer


def run_calc_game():
    engine_game_start(GAME_GREET_CALC, give_question_and_answer)
