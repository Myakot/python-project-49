from math import gcd
from brain_games.consts import TASK_GCD
from brain_games.utils import generate_num
from brain_games.engine import engine_game_start


def give_question_answer():
    correct_answer, number1, number2 = check_gcd()
    question = f'{number1} {number2}'
    return correct_answer, question


def check_gcd():
    number1, number2 = generate_num(), generate_num()
    correct_answer = str(gcd(number1, number2))
    return correct_answer, number1, number2


def run_gcd_game():
    engine_game_start(TASK_GCD, give_question_answer)
