from random import randint
import brain_games.constants


desc = brain_games.constants.PRIME


def is_prime(number):
    for element in range(2, int(number ** 1 / 2) + 1):
        if number % element == 0:
            return False
    return True


def create_question_answer():
    number = randint(1, 101)
    if is_prime(number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number
