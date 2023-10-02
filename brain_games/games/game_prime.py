from brain_games.consts import GAME_GRT_PRIME
from brain_games.utils import get_random_num
from brain_games.engine import engine_game_start


def give_question_and_answer():
    number = get_random_num()
    correct_answer = 'yes' if is_prime(number) is True else 'no'
    return correct_answer, number


def is_prime(number):
    for element in range(2, int(number ** 0.5) + 1):
        if number % element == 0:
            return False
    return True


def run_prime_game():
    engine_game_start(GAME_GRT_PRIME, give_question_and_answer)
