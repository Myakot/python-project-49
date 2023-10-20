from brain_games.consts import GAME_GREET_EVEN
from brain_games.utils import get_random_num
from brain_games.engine import run_game


def is_even(question):
    return question % 2 == 0


def get_even_question_and_result():
    problem_num = get_random_num()
    сorrect_answer = 'yes' if is_even(problem_num) is True else 'no'
    return сorrect_answer, problem_num


def run_even_game():
    run_game(GAME_GREET_EVEN, get_even_question_and_result)
