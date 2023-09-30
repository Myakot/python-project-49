from brain_games.consts import GAME_GREET_EVEN
from brain_games.utils import get_random_num
from brain_games.engine import engine_game_start


def give_question_answer():
    question = get_random_num()
    сorrect_answer = check_even(question)
    return сorrect_answer, question


def check_even(question):
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer


def run_even_game():
    engine_game_start(GAME_GREET_EVEN, give_question_answer)
