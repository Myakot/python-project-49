#!/usr/bin/env python3


import random


def brain_greet():
    # Приветствие и вывод задачи
    global name
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # эту функцию в движок надо < --------------------------------------------
    # от скрипта должен передаваться только Принт №3


def brain_generate():
    # Генерация числа для задачи
    global gen_number_a
    global gen_number_b
    arithmetics = ['+', '-', '*']
    gen_number_a = random.randint(1, 99999)
    gen_number_b = random.randint(-99999, 1)
    gen_arithmetics = random.choice(arithmetics)
    return [gen_number_a, gen_number_b, gen_arithmetics]
    # ЭКСПОРТ = LIST = ЕГО НАДО РАСПАКОВЫВАТЬ, ЧТОБЫ ИСПОЛЬЗОВАТЬ
    # эту функцию в движок надо < --------------------------------------------
    # от скрипта должен передаваться список математических операций


def brain_answer_find():
    # Определение правильного ответа
    global correct_answer

    # это условие if для brain_calc
    match brain_generate()[2]:
        case '+':
            correct_answer = brain_generate()[0] + brain_generate()[1]
        case '-':
            correct_answer = brain_generate()[0] - brain_generate()[1]
        case _:
            correct_answer = brain_generate()[0] * brain_generate()[1]
    return correct_answer

    # это условие if для brain_even
    if gen_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer

    # эту функцию в движок надо < -----------------------------
    # из скрипта должна идти информация о названии игры, в зависимости
    # от названия игры - будет выбираться условие if


def brain_engine_question():
    # if game_name = 'игра even':
    question = gen_number
    return question
    # if game_name = 'игра calc':
    question = brain_generate()[0], brain_generate()[2], brain_generate()[1]
    # ^ скорей всего не сработает, но это распаковка списка на пример 1+1


def brain_engine_input():
    # Принятие ответа в условии переданным скриптом только - НЕ ЦИКЛИТЬ - ВЫВОДИТЬ В КОНЕЦ ИГРЫ НЕПРАВИЛЬНЫЙ ОТВЕТ
    global user_answer
    # Товарищ наставник - нужна помощь с global - это костыль, как лучше?
    print(f'Question: {gen_number}')
    user_answer = input('Your answer: ')
    if user_answer == 'yes' or user_answer == 'no':
        return user_answer
    else:
        print('Ошибка ввода: неправильный ответ')
        brain_even_input()

# В случае, если пользователь даст неверный ответ, необходимо вывести:
#
# Question: 25 * 7
# Your answer: 145
# '145' is wrong answer ;(. Correct answer was '175'.
# Let's try again, Sam!

# brain-calc
#
# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# What is the result of the expression?
# Question: 4 + 10
# Your answer: 14
# Correct!
# Question: 25 - 11
# Your answer: 14
# Correct!
# Question: 25 * 7
# Your answer: 175
# Correct!
# Congratulations, Sam!