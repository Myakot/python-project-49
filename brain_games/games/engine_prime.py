from random import randint


GAME_DESC = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def create_question_answer():
    num = randint(1, 11)
    if num == 1:
        correct_answer = 'no'
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, num
