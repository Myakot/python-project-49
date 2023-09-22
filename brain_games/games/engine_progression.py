from random import randint, choice
from brain_games.constants import DESC_GCD


desc = DESC_GCD


def create_question_answer():
    sequence = create_sequence()
    correct_answer = choice(sequence)
    index_s = sequence.index(correct_answer)
    question = sequence[:index_s] + ['..'] + sequence[index_s + 1:]
    question = ' '.join(str(item) for item in question)
    return str(correct_answer), question


def create_sequence():
    seq_length = randint(5, 10)
    seq_step = randint(1, 100)
    sequence = [randint(1, 100)]
    iterator_x = 0
    while iterator_x <= seq_length:
        sequence.append(sequence[iterator_x] + seq_step)
        iterator_x += 1
    return sequence
