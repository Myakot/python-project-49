from brain_games.engine import get_initial_randomized_number
from brain_games.engine import welcome_get_name
from brain_games.engine import getting_user_answer
from brain_games.engine import show_correct_answer
from brain_games.engine import return_win_end
from random import choice
from random import randint


def question_answer_sequence(sequence):
    answer = choice(sequence)
    i = sequence.index(answer)
    sequence_question = sequence[:i] + ['..'] + sequence[i + 1:]
    sequence_question = ' '.join(str(x) for x in sequence_question)
    return sequence_question, answer


def current_sequence():
    seq_length = randint(5, 10)
    seq_step = get_initial_randomized_number()
    sequence = [get_initial_randomized_number()]
    x = 0
    while x <= seq_length:
        sequence.append(sequence[x] + seq_step)
        x += 1
    return sequence


def main():
    print('What number is missing in the progression?')
    user_name = welcome_get_name()
    counter = 0
    while counter < 3:
        question = question_answer_sequence(current_sequence())
        (sequence_question, answer) = question
        correct_answer = answer
        print(f'Question: {sequence_question.strip()}')
        user_answer = getting_user_answer()
        if str(correct_answer) == user_answer:
            print("Correct!\n")
            counter += 1
        else:
            show_correct_answer(user_answer, correct_answer, user_name)
            return

    if counter == 3:
        return_win_end(user_name)
