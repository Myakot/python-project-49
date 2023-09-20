from random import randint
from math import gcd


GAME_DESC = 'Find the greatest common divisor of given numbers.'


def create_question_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    correct_answer = str(gcd(num1, num2))
    question = f'{num1} {num2}'

    return correct_answer, question
