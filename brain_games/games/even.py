from brain_games.consts import GAME_GREET_EVEN
from brain_games.utils import get_random_num
from brain_games.engine import run_game


def get_question_and_answer():
    question = get_random_num()
    сorrect_answer = 'yes' if is_even(question) is True else 'no'
    return сorrect_answer, question


def is_even(question):
    return True if question % 2 == 0 else False


def run_even_game():
    run_game(GAME_GREET_EVEN, get_question_and_answer)
