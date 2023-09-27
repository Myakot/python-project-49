from brain_games.consts import DESC_PRIME
from brain_games.utils import generate_num
from brain_games.engine import engine_game_start


def is_prime(number):
    for element in range(2, int(number ** 0.5) + 1):
        if number % element == 0:
            return False
    return True


def create_question_answer():
    number = generate_num()
    correct_answer = 'yes' if is_prime(number) is True else 'no'
    return correct_answer, number


def run_prime_game():
    engine_game_start(DESC_PRIME, create_question_answer)
