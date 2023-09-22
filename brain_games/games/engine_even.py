from random import randint
from brain_games.consts import DESC_EVEN


def create_question_answer():
    question = randint(0, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question


def print_game_desc():
    desc = DESC_EVEN
    print(desc)
