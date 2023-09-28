from math import gcd
from brain_games.consts import TASK_GCD
from brain_games.utils import generate_num
from brain_games.engine import engine_game_start


def create_question_answer():
    number1 = generate_num()
    number2 = generate_num()
    # Тут вынести функцию проверки числа

    correct_answer = str(gcd(number1, number2))
    question = f'{number1} {number2}'
    return correct_answer, question


def run_gcd_game():
    engine_game_start(TASK_GCD, create_question_answer)
