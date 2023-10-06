from random import choice
from brain_games.consts import GAME_GREET_CALC
from brain_games.utils import get_random_num
from brain_games.engine import run_game


# Модуль random python программисты предпочитают использовать
# через квалификационное имя, тк имена у функций, слишком общие.

# Функцию вычисления в данном случае предпочтительно объявить
# выше, нежели где она используется, так будет удобнее, если
# следующий разработчик захочет поэкспериментировать и не
# столкнётся с исключением, что функция не объявлена

# И наверное самое важное - именование, знаю, в каждом ревью
# упоминаю, но это будет преследовать каждого разработчика)
# Всю карьеру будет встречаться момент, когда на придумывание
# название может уйти половину времени от реализации :D . Как
# на счёт get_math_question_and_result, как по мне - полностью
# говоряще. А для вычисления get_random_math_sign_and_result(забегая вперёд)

# Во вспомогательной функции check_for_answer - лучше там и вычислять
# рандомный знак и тд, так же его и возвращать. (get_random_math_sign_and_result)
def get_question_and_answer():
    number1, number2 = get_random_num(), get_random_num()
    sign = choice(['+', '-', '*'])
    question = f'{number1} {sign} {number2}'
    correct_answer = check_for_answer(number1, sign, number2)
    return correct_answer, question


def check_for_answer(number1, sign, number2):
    match sign:
        case '*':
            correct_answer = number1 * number2
        case '-':
            correct_answer = number1 - number2
        case '+':
            correct_answer = number1 + number2
    return str(correct_answer)


def run_calc_game():
    run_game(GAME_GREET_CALC, get_question_and_answer)
