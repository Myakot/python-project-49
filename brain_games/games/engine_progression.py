from random import randint, choice


GAME_DESC = 'What number is missing in the progression?'


def create_question_answer():
    sequence = current_sequence()
    correct_answer = choice(sequence)
    i = sequence.index(correct_answer)
    question = sequence[:i] + ['..'] + sequence[i + 1:]
    question = ' '.join(str(x) for x in question)
    return str(correct_answer), question


def current_sequence():
    seq_length = randint(5, 10)
    seq_step = randint(1, 100)
    sequence = [randint(1, 100)]
    x = 0
    while x <= seq_length:
        sequence.append(sequence[x] + seq_step)
        x += 1
    return sequence
