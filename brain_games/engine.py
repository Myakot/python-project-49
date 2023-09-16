import prompt
from random import randint


def get_initial_randomized_number():
    return randint(1, 10)


def getting_user_answer():
    return prompt.string('Your answer: ')


def show_correct_answer(us_ans, cor_ans, user_name):
    print(f"'{us_ans}' is wrong answer ;(. Correct answer was '{cor_ans}'.")
    print(f"Let's try again, {user_name}!")
    return  # Hard reset / Program exit


def return_win_end(user_name):
    print(f'Congratulations, {user_name}!')
    return  # Program exit
