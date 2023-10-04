from math import gcd
from brain_games.consts import GAME_GREET_GCD
from brain_games.utils import get_random_num
from brain_games.engine import run_game


def get_question_and_answer():
    correct_answer, number1, number2 = get_gcd()
    question = f'{number1} {number2}'
    return correct_answer, question


def get_gcd():
    number1, number2 = get_random_num(), get_random_num()
    correct_answer = str(gcd(number1, number2))
    return correct_answer, number1, number2


def run_gcd_game():
    run_game(GAME_GREET_GCD, get_question_and_answer)
