import prompt
from random import randint


def get_initial_randomized_number():
    return randint(1, 500)


def getting_user_answer():
    return prompt.string('Your answer: ')


def show_correct_answer(user_answer, correct_answer, user_name):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    # ^^ Линтер ругается на 8 лишних символов, стоит ли резать строку? Нечитаемо
    print(f"Let's try again, {user_name}!")
    return  # Hard reset / Program exit


def return_win_end(user_name):
    print(f'Congratulations, {user_name}!')
    return  # Program exit
