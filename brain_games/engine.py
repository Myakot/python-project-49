import prompt
from brain_games.consts import ATTEMPT_COUNTER
from brain_games.consts import TO_WIN

# Вот тут некоторые принты можно объединить, и проход
# по раундам игры сделать через for - чтобы не исменять константу:


def engine_game_start(task_description, create_question_answer):
    counter = ATTEMPT_COUNTER
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(task_description)
    while counter < TO_WIN:
        correct_answer, question = create_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.'
                  f"\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
