import prompt
import brain_games.constants


def welcome_get_name():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def engine_play(game):
    user_name = welcome_get_name()
    print(game.desc)
    while brain_games.constants.COUNTER < 3:
        correct_answer, question = game.create_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            brain_games.constants.COUNTER += 1
        else:
            print(f'{user_answer} is wrong answer ;(.')
            print(f'Correct answer was {correct_answer}.')
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
