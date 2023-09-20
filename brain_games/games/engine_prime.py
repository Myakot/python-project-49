from brain_games.engine import get_initial_randomized_number
from brain_games.engine import welcome_get_name
from brain_games.engine import getting_user_answer
from brain_games.engine import show_correct_answer
from brain_games.engine import return_win_end


def current_correct_answer(num):
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
    return correct_answer


def current_question():
    num = get_initial_randomized_number()
    return num


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    user_name = welcome_get_name()
    counter = 0
    while counter < 3:
        question = current_question()
        correct_answer = current_correct_answer(question)
        print(f'Question: {question}')
        user_answer = getting_user_answer()
        if correct_answer == user_answer:
            print("Correct!\n")
            counter += 1
        else:
            show_correct_answer(user_answer, correct_answer, user_name)
        return

    if counter == 3:
        return_win_end(user_name)
