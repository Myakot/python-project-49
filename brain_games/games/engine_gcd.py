from random import randint
from math import gcd
from brain_games.consts import DESC_GCD


def create_question_answer():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    correct_answer = str(gcd(number1, number2))
    question = f'{number1} {number2}'

    return correct_answer, question


def print_game_desc():
    desc = DESC_GCD
    print(desc)
