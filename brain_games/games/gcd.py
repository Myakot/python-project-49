from math import gcd
from brain_games.consts import GAME_GREET_GCD
from brain_games.utils import get_num
from brain_games.engine import run_game


def get_gcd():
    number1, number2 = get_num(), get_num()
    correct_answer = str(gcd(number1, number2))
    return correct_answer, number1, number2


def get_gcd_question_and_result():
    correct_answer, number1, number2 = get_gcd()
    question = f'{number1} {number2}'
    return correct_answer, question


def run_gcd_game():
    run_game(GAME_GREET_GCD, get_gcd_question_and_result)
