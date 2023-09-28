from brain_games.consts import TASK_EVEN
from brain_games.utils import generate_num
from brain_games.engine import engine_game_start


def give_question_answer():
    question = generate_num()
    сorrect_answer = check_even(question)
    return сorrect_answer, question


def check_even(question):
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer


def run_even_game():
    engine_game_start(TASK_EVEN, give_question_answer)
