from random import randint


GAME_DESCRIPTION = ('Answer "yes" if given number is prime.'
                    ' Otherwise answer "no".')


def is_prime(number):
    for element in range(2, int(number ** 1 / 2) + 1):
        if number % element == 0:
            return False
    return True


def create_question_answer():
    number = randint(1, 11)
    if is_prime(number) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number
