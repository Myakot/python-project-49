import random
from brain_games.consts import GAME_GREET_PROGRESSION
from brain_games.consts import PROGRESSION_SEQUENCE_LENGTH
from brain_games.utils import get_random_num
from brain_games.engine import run_game


def generate_progression_items():
    seq_start, seq_step = get_random_num(), get_random_num()
    seq_length = PROGRESSION_SEQUENCE_LENGTH
    return seq_start, seq_step, seq_length


def generate_progression():
    sequence = []
    seq_start, seq_step, seq_length = generate_progression_items()
    for i in range(seq_start, seq_length, seq_step):
        sequence.append(i)
    return sequence


def get_progression_and_missing_num():
    sequence = generate_progression()
    correct_answer = random.choice(sequence)
    index_s = sequence.index(correct_answer)
    question = sequence[:index_s] + ['..'] + sequence[index_s + 1:]
    question = ' '.join(str(item) for item in question)
    return str(correct_answer), question


def run_progression_game():
    run_game(GAME_GREET_PROGRESSION, get_progression_and_missing_num)
