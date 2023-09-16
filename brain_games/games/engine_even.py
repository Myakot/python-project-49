from brain_games import cli, engine


def current_correct_answer(question):
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    user_name = cli.welcome_get_name()
    counter = 0
    while counter < 3:
        question = engine.get_initial_randomized_number()
        correct_answer = current_correct_answer(question)
        print(f'Question: is {question} even')
        user_answer = engine.getting_user_answer()
        if correct_answer == user_answer:
            print("Correct!\n")
            counter += 1
        else:
            engine.show_correct_answer(user_answer, correct_answer, user_name)
            return  # Hard reset upon wrong answer

    if counter == 3:
        engine.return_win_end(user_name)
