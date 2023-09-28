#!/usr/bin/env python3


from brain_games.cli import welcome_get_name


def main():
    print('Welcome to the Brain Games!')
    welcome_get_name()


if __name__ == '__main__':
    main()


# В файле brain_games.py используется функция welcome_get_name, хотя по сути мы
# не берём имя да и не приветсвуем там, поэтому следует назвать как было по
# заданию и мы уёдем от двух моментов ненужных

# #!/usr/bin/env python3
#
#
# from brain_games.cli import welcome_get_name
#
#
# def main():
#     print('Welcome to the Brain Games!')
#     welcome_get_name()
#
#
# if __name__ == '__main__':
#     main()
