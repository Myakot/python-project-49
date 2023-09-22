from brain_games.consts import DESC_EVEN
from brain_games.utils import random_num


def create_question_answer():
    question = random_num()
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer, question


def print_game_desc():
    desc = DESC_EVEN
    print(desc)
