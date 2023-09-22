#!/usr/bin/env python3


from brain_games.engine import engine_game_start
from brain_games.games import engine_gcd


def main():
    engine_game_start(engine_gcd)


if __name__ == '__main__':
    main()
