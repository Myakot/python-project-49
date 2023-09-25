from math import gcd
from brain_games.consts import DESC_GCD
from brain_games.utils import random_num
from brain_games.engine import engine_game_start


def create_question_answer():
    number1 = random_num()
    number2 = random_num()
    correct_answer = str(gcd(number1, number2))
    question = f'{number1} {number2}'
    return correct_answer, question


def run_gcd_game():
    engine_game_start(DESC_GCD, create_question_answer)
