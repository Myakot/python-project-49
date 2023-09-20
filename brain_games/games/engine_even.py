from random import randint
import brain_games.constants


desc = brain_games.constants.EVEN


def create_question_answer():
    question = randint(0, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
