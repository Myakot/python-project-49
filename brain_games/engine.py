import prompt
from brain_games.consts import NUM_OF_GAMES


def run_game(task_description, get_question_and_answer):
    # Раз уж объединяешь строчки в движке, тут тоже можно объединить:
    #
    #     print('Welcome to the Brain Games!')
    #     user_name = prompt.string('May I have your name? ')
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!\n{task_description}')
    for _ in range(NUM_OF_GAMES):
        correct_answer, question = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            # Тут же экранизацию переноса строки лучше сделать в конце первой, а не в
            # начале второй, таково соглашение разработчиков, для удобства:
            #
            #             print(f'{user_answer} is wrong answer ;(.'f'Correct answer
            #             was {correct_answer}.'f"\nLet's try again, {user_name}!")
            print(f'{user_answer} is wrong answer ;(.'
                  f'Correct answer was {correct_answer}.'
                  f"\nLet's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
#