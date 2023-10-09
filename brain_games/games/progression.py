from random import choice
from brain_games.consts import GAME_GREET_PROGRESSION
from brain_games.consts import PROGRESSION_SEQUENCE_LENGTH
from brain_games.utils import get_num
from brain_games.engine import run_game


def create_sequence():
    seq_length = PROGRESSION_SEQUENCE_LENGTH
    seq_step, sequence_start = get_num(), get_num()
    sequence = []
    for index in range(seq_length):
        sequence_start += seq_step
        sequence.append(sequence_start)
    return sequence


def get_progression_and_missing_num():
    sequence = create_sequence()
    correct_answer = choice(sequence)
    index_s = sequence.index(correct_answer)
    question = sequence[:index_s] + ['..'] + sequence[index_s + 1:]
    question = ' '.join(str(item) for item in question)
    return str(correct_answer), question


def run_progression_game():
    run_game(GAME_GREET_PROGRESSION, get_progression_and_missing_num)