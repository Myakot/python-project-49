import random
from brain_games.consts import GAME_GREET_PROGRESSION
from brain_games.consts import PROGRESSION_SEQUENCE_LENGTH
from brain_games.utils import get_random_num
from brain_games.engine import run_game


def generate_progression_items():
    seq_start, seq_step = get_random_num(), get_random_num()
    seq_length = PROGRESSION_SEQUENCE_LENGTH
    return generate_progression(seq_start, seq_step, seq_length)


def generate_progression(seq_start, seq_step, seq_length):
    return [seq_start + i * seq_step for i in range(seq_length)]


def get_progression_and_missing_num():
    sequence = generate_progression_items()
    index_s = random.randint(0, len(sequence) - 1)
    replaced_number = sequence[index_s]
    sequence[index_s] = '..'
    return str(replaced_number), str(sequence)


def run_progression_game():
    run_game(GAME_GREET_PROGRESSION, get_progression_and_missing_num)
