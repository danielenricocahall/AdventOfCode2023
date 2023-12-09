import re
from typing import List, Dict


def navigate_map(_map: Dict[str, List[str]], directions: str):
    steps = 0
    current_node = next(k for k in _map.keys())
    directions_counter = 0
    while current_node != 'ZZZ':
        steps += 1
        index = 0 if directions[directions_counter] == 'L' else 1
        current_node = _map[current_node][index]
        directions_counter = (directions_counter + 1) % len(directions)
    return steps


def convert_map_to_lookup_structure(_map: List[str]) -> Dict[str, List[str]]:
    return {node: re.sub(r'[(),]', '', left_and_right_nodes).split() for node, left_and_right_nodes in map(lambda x: x.split(" = "), _map)}


if __name__ == "__main__":
    with open('input.txt') as fp:
        directions_and_map = list(filter(lambda s: s, map(str.strip, fp.readlines())))
        directions, *_map = directions_and_map
        _map = convert_map_to_lookup_structure(_map)
        number_of_steps = navigate_map(_map, directions)
        print(number_of_steps)