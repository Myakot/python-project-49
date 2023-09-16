from brain_games import cli, engine
from math import gcd


def current_correct_answer(num1, num2):
    correct_answer = str(int(gcd(num1, num2)))
    # print(f'Помощь, чтобы не позориться: correct-answer = {correct_answer}')
    # print(f'DEBUG, correct-answerTYPE = {type(correct_answer)}')
    return correct_answer


def current_case():
    num1 = engine.get_initial_randomized_number()
    num2 = engine.get_initial_randomized_number()
    return num1, num2


def main():
    print('Find the greatest common divisor of given numbers.')
    user_name = cli.welcome_get_name()
    counter = 0
    while counter < 3:
        question = current_case()
        (num1, num2) = question
        correct_answer = current_correct_answer(num1, num2)
        print(f'Question: {num1} {num2}')
        user_answer = engine.getting_user_answer()
        # print(f'DEBUG, USER-ANSWERTYPE = {type(user_answer)}')
        if correct_answer == user_answer:
            print("Correct!\n")
            counter += 1
        else:
            engine.show_correct_answer(user_answer, correct_answer, user_name)
            return  # Hard reset upon wrong answer

    if counter == 3:
        engine.return_win_end(user_name)