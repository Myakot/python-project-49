from random import choice
from brain_games.consts import TASK_PROGRESSION
from brain_games.consts import PROGRESSION_SEQUENCE_LENGTH
from brain_games.utils import generate_num
from brain_games.engine import engine_game_start


def give_question_answer():
    # Создание правильного ответа + вопроса
    sequence = create_sequence()
    correct_answer = choice(sequence)
    index_s = sequence.index(correct_answer)
    question = sequence[:index_s] + ['..'] + sequence[index_s + 1:]
    question = ' '.join(str(item) for item in question)
    return str(correct_answer), question


def create_sequence():
    # Создание последовательности
    seq_length = PROGRESSION_SEQUENCE_LENGTH
    seq_step, sequence_start = generate_num(), generate_num()
    sequence = []
    for index in range(seq_length):
        sequence_start += seq_step
        sequence.append(sequence_start)
    return sequence


def run_progression_game():
    engine_game_start(TASK_PROGRESSION, give_question_answer)
