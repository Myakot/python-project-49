#!/usr/bin/env python3
# В данном файле должна быть импортирована лишь одна функция,
# которая запускает игры
# Тут же мы импортируем целый модуль и движок
# во всех скриптах


from brain_games.engine import engine_game_start
from brain_games.games import engine_calc


def main():
    engine_game_start(engine_calc)


if __name__ == '__main__':
    main()
