from random import randint


GAME_DESC = 'Answer "yes" if the number is even, otherwise answer "no".'


def create_question_answer():
    question = randint(0, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
