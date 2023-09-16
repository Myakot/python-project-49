from brain_games import cli, engine
from random import choice
from random import randint


def question_answer_sequence(sequence):
    answer = choice(sequence)
    i = sequence.index(answer)
    # print(f'DEBUG - INDEX CHOICE {i}')
    sequence_question = sequence[:i]+['..']+sequence[i+1:]
    # print(f'DEBUG - SEQUENCE_QUESTION = {sequence_question}')
    print(f'DEBUG - QUESTION = {answer}')
    return sequence_question, answer


def current_sequence():
    seq_length = randint(2, 7)
    # print(f'DEBUG SEQ_LENGTH = {seq_length}')
    seq_step = engine.get_initial_randomized_number()
    # print(f'DEBUG SEQUENCE STEP {seq_step}')
    sequence = [engine.get_initial_randomized_number()]
    # print(f'DEBUG INITIAL SEQ - {sequence}')
    x = 0
    while x <= seq_length:
        sequence.append(sequence[x] + seq_step)
        # print(sequence, '-DEBUG EACH SEQ STEP')
        x += 1
    return sequence


def main():
    print('What number is missing in the progression?')
    user_name = cli.welcome_get_name()
    counter = 0
    while counter < 3:
        question = question_answer_sequence(current_sequence())
        (sequence_question, answer) = question
        # print(f'DEBUG - UNPACKING ANSWER AND QUESTION')
        correct_answer = answer
        print(f'Question: {sequence_question}')
        user_answer = engine.getting_user_answer()
        if str(correct_answer) == user_answer:
            print("Correct!\n")
            counter += 1
        else:
            engine.show_correct_answer(user_answer, correct_answer, user_name)
            return  # Hard reset upon wrong answer

    if counter == 3:
        engine.return_win_end(user_name)

# Показываем игроку ряд чисел, который образует арифметическую прогрессию, заменив любое из чисел двумя точками. Игрок должен определить это число.
# Рекомендуемая длина прогрессии – 10 чисел. Длина может генерироваться случайным образом, но должна содержать не менее пяти чисел
# Позиция спрятанного элемента каждый раз изменяется — выбирается случайным образом

# brain-progression
# Welcome to the Brain Games!
# May I have your name? Sam
# Hello, Sam!
# What number is missing in the progression?
# Question: 5 7 9 11 13 .. 17 19 21 23
# Your answer: 15
# Correct!
# Question: 2 5 8 .. 14 17 20 23 26 29
# Your answer: 11
# Correct!
# Question: 14 19 24 29 34 39 44 49 54 ..
# Your answer: 59
# Correct!
# Congratulations, Sam!