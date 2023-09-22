from brain_games.consts import DESC_PRIME
from brain_games.utils import random_num


def is_prime(number):
    for element in range(2, int(number ** 0.5) + 1):
        if number % element == 0:
            return False
    return True


def create_question_answer():
    number = random_num()
    correct_answer = 'yes' if is_prime(number) is True else 'no'
    return correct_answer, number


def print_game_desc():
    desc = DESC_PRIME
    print(desc)
