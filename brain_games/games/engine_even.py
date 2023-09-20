from brain_games.engine import get_initial_randomized_number
from brain_games.engine import welcome_get_name
from brain_games.engine import getting_user_answer
from brain_games.engine import show_correct_answer
from brain_games.engine import return_win_end


def current_correct_answer(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    user_name = welcome_get_name()
    counter = 0
    while counter < 3:
        question = get_initial_randomized_number()
        correct_answer = current_correct_answer(question)
        print(f'Question: {question}')
        user_answer = getting_user_answer()
        if correct_answer == user_answer:
            print("Correct!")
            counter += 1
        else:
            show_correct_answer(user_answer, correct_answer, user_name)
            return

    if counter == 3:
        return_win_end(user_name)
