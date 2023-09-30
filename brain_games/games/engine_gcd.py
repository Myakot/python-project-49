from math import gcd
from brain_games.consts import GAME_GREET_GCD
from brain_games.utils import get_random_num
from brain_games.engine import engine_game_start


def give_question_answer():
    correct_answer, number1, number2 = check_gcd()
    question = f'{number1} {number2}'
    return correct_answer, question


def check_gcd():
    number1, number2 = get_random_num(), get_random_num()
    correct_answer = str(gcd(number1, number2))
    return correct_answer, number1, number2


def run_gcd_game():
    engine_game_start(GAME_GREET_GCD, give_question_answer)
