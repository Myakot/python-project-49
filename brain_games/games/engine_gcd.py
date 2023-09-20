from random import randint
from math import gcd
import brain_games.constants


desc = brain_games.constants.GCD


def create_question_answer():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    correct_answer = str(gcd(number1, number2))
    question = f'{number1} {number2}'

    return correct_answer, question
