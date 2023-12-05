import operator
import re
from collections import defaultdict
from functools import reduce
from typing import Dict, List

GAME_ID_PATTERN = re.compile(r'(?<=Game\s)\d+')
MAX_COLOR_TO_COUNT = {"red": 12, "green": 13, "blue": 14}
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def count_games_possible(games: List[str]) -> int:
    game_id_sum = 0
    game_ids = [int(GAME_ID_PATTERN.search(game).group(0)) for game in games]
    for game_id, game in zip(game_ids, games):
        game = re.sub(r'Game\s\d+:', '', game).strip()
        if game_is_possible(game):
            game_id_sum += game_id
    return game_id_sum


def game_is_possible(game: str) -> bool:
    for cube_set in game.split(";"):
        color_to_count = compute_color_to_count(cube_set)
        for color in ("red", "green", "blue"):
            if color_to_count.get(color, 0) > MAX_COLOR_TO_COUNT[color]:
                return False
    return True

def compute_sum_of_power(games: List[str]) -> int:
    return sum(compute_power_for_game(game) for game in games)



def compute_power_for_game(game: str) -> int:
    game = re.sub(r'Game\s\d+:', '', game).strip()  # copy and paste baby
    minimum_required_colors = defaultdict(int)
    for cube_set in game.split(";"):
        color_to_count = compute_color_to_count(cube_set)
        for color, count in color_to_count.items():
            minimum_required_colors[color] = max(minimum_required_colors[color], count)
    return reduce(operator.mul, minimum_required_colors.values())



def compute_color_to_count(cube_set: str) -> Dict[str, int]:
    cubes = cube_set.strip().split(", ")
    color_to_count = dict(map(lambda x: x.split(" ")[::-1], cubes))
    color_to_count = {k: int(v) for k, v in color_to_count.items()}
    return color_to_count


if __name__ == "__main__":
    with open('./input.txt') as fp:
        games = list(map(str.strip, fp.readlines()))
    print(count_games_possible(games))
    print(compute_sum_of_power(games))
