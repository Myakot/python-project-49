import prompt
from brain_games.consts import NUM_OF_GAMES


def run_game(task_description, get_question_and_answer):
    user_name = prompt.string('Welcome to the Brain Games!\n'
                              'May I have your name? ')
    print(f'Hello, {user_name}!\n{task_description}')
    for _ in range(NUM_OF_GAMES):
        correct_answer, question = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(.'
                  f'Correct answer was {correct_answer}.\n'
                  f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
