from brain_games.consts import DESC_EVEN
from brain_games.utils import generate_num
from brain_games.engine import engine_game_start


def create_question_answer():
    question = generate_num()
    # Тут вынести функцию проверки числа на чётность

    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer, question


def run_even_game():
    engine_game_start(DESC_EVEN, create_question_answer)
