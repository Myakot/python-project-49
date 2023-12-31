from brain_games.consts import GAME_GREET_PRIME
from brain_games.utils import get_random_num
from brain_games.engine import run_game


def is_prime(number):
    for element in range(2, int(number ** 0.5) + 1):
        if number % element == 0:
            return False
    return True


def get_prime_question_and_result():
    number = get_random_num()
    correct_answer = 'yes' if is_prime(number) is True else 'no'
    return correct_answer, number


def run_prime_game():
    run_game(GAME_GREET_PRIME, get_prime_question_and_result)
