import prompt
from .consts import COUNTER
# Лучше импортировать с полным указанием пути, а не через точку
# from .consts import COUNTER



# Вот тут некоторые принты можно объединить, и проход
# по раундам игры сделать через for - чтобы не исменять константу:

# Так же сюда относиться название COUNTER - не совсем понятно,
# что за счётчик, нужно назвать более описательно, так же осталась
# конструкция while counter < 3: , где присутствует "магическое" число

# Слово desc часто используется в качестве направления
# сортировки, поэтому стоит переименовать

def engine_game_start(desc, create_question_answer):
    counter = COUNTER
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(desc)
    while counter < 3:
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
