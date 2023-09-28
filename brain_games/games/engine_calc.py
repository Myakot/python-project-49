from random import choice
from brain_games.consts import TASK_CALC
from brain_games.utils import generate_num
from brain_games.engine import engine_game_start


def give_question_answer():
    number1, number2 = generate_num(), generate_num()
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
    engine_game_start(TASK_CALC, give_question_answer)
