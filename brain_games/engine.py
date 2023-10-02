import prompt
from brain_games.consts import NUM_OF_GAMES


def engine_game_start(task_description, give_question_and_answer):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n{task_description}')
    for _ in range(NUM_OF_GAMES):
        correct_answer, question = give_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(.'
                  f'Correct answer was {correct_answer}.'
                  f"\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
