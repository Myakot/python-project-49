from random import choice, randint


GAME_DESC = 'What is the result of the expression?'


def create_question_answer():
    num1 = randint(-100, 100)
    num2 = randint(-100, 100)
    sign = choice(['+', '-', '*'])
    question = f'{num1} {sign} {num2}'
    print(f'DEBUG, {question} = question')

    if sign == '*':
        correct_answer = str(num1 * num2)
    elif sign == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 + num2)
    print(f'DEBUG, {correct_answer}, {question} = correct_answer, question IN ENGINE_CALC.PY')
    return correct_answer, question
