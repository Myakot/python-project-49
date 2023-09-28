from prompt import string
from brain_games.consts import TO_WIN


def engine_game_start(task_description, give_question_answer):
    print('Welcome to the Brain Games!')
    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}!\n'
          f'{task_description}')
    play_rounds(give_question_answer, user_name)


def play_rounds(give_question_answer, user_name):
    for ATTEMPT_COUNTER in range(TO_WIN):
        correct_answer, question = give_question_answer()
        print(f'Question: {question}')
        user_answer = string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.'
                  f"\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
