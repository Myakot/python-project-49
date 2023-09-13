#!/usr/bin/env python3


import random


def brain_even():
    # main body
    brain_even_greet()  # greet user
    brain_even_game()  # game itself
    return
    # brain_game()  # return to game selection


def brain_even_greet():
    # Приветствие и вывод задачи
    global name
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # Нужно где-то указать правила игры, позже,
    # если в задаче такое будет, особенно про 3 yes


def brain_even_game():
    correct_counter = 0
    while correct_counter <= 2:
        brain_even_generate()  # get gen_number
        brain_even_answer_find()  # get correct_answer
        brain_even_input()  # get user_answer
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            brain_even()  # Hard reset
        else:
            print('Correct!')
            correct_counter += 1
            # print(correct_counter, 'correct_counter -----')
    else:
        print(f'Congratulations, {name}!')
    return


def brain_even_generate():
    # Генерация числа для задачи
    global gen_number
    gen_number = random.randint(1, 99999)
    return gen_number


def brain_even_answer_find():
    # Определение правильного ответа
    global correct_answer
    if gen_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def brain_even_input():
    # Принятие ответа либо "yes" либо "no" - циклить
    global user_answer
    # Товарищ наставник - нужна помощь с global - это костыль, как лучше?
    print(f'Question: {gen_number}')
    user_answer = input('Your answer: ')
    if user_answer == 'yes' or user_answer == 'no':
        return user_answer
    else:
        print('Ошибка ввода: неправильный ответ')
        brain_even_input()


# --------------
# Не подходит под задачу: "Любой некорректный ввод считается ошибкой,
# например, n, и равносилен неправильному ответу."
# захотелось сразу сделать, чтобы тестировать
# было проще и если такая цель будет потом.
#     while True:
#         print(f'Question: {gen_number}')
#         user_answer = input('Your answer: ')
#         if user_answer == 'yes' or user_answer == 'no':
#             break
#         else:
#             print('You can either say "yes" or "no"')
#             continue
#     return user_answer
# --------------


if __name__ == '__main__':
    brain_even()
