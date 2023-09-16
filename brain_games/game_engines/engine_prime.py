from brain_games import cli, engine


def current_correct_answer(num):
    if num == 1:
        correct_answer = 'no'
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print(f'DEBUG. correct-answer = {correct_answer}')
    # print(f'DEBUG, correct-answerTYPE = {type(correct_answer)}')
    return correct_answer


def current_question():
    num = engine.get_initial_randomized_number()
    return num


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    user_name = cli.welcome_get_name()
    counter = 0
    while counter < 3:
        question = current_question()
        correct_answer = current_correct_answer(question)
        print(f'Question: {question}')
        user_answer = engine.getting_user_answer()
        if correct_answer == user_answer:
            print("Correct!\n")
            counter += 1
        else:
            engine.show_correct_answer(user_answer, correct_answer, user_name)
            return  # Hard reset upon wrong answer

    if counter == 3:
        engine.return_win_end(user_name)
