from random import randint


GAME_DESCRIPTION = ('Answer "yes" if given number is prime.'
                    ' Otherwise answer "no".')


def create_question_answer():
    number = randint(1, 11)
    print(len(GAME_DESCRIPTION))
    if number == 1:
        correct_answer = 'no'
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number
