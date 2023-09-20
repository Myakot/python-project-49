import prompt


def welcome_get_name():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def engine_main(game):  # Сюда возвращается correct_answer + question
    user_name = welcome_get_name()
    print(f'DEBUG, {user_name} = user_name')
    print(game.GAME_DESC)
    print(f'DEBUG, {game.GAME_DESC} = game_desc')
    COUNTER = 0
    while COUNTER < 3:
        correct_answer, question = game.create_question_answer()
        print(f'DEBUG, {correct_answer} = correct_answer')
        print(f'DEBUG, {question} = question')
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        print(f'DEBUG, {user_answer} = user_answer')
        if user_answer == correct_answer:
            print('Correct!')
            COUNTER += 1
            print(f'DEBUG, {COUNTER} = COUNTER')
        else:
            print(f'{user_answer} is wrong answer ;(.')
            print(f'Correct answer was {correct_answer}.')
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
