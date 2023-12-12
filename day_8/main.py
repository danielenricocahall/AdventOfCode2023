import re
from functools import lru_cache
from typing import List, Dict, Tuple


def navigate_map(_map: Dict[str, List[str]], directions: str) -> int:
    steps = 0
    current_node = 'AAA'
    directions_counter = 0
    while current_node != 'ZZZ':
        steps += 1
        index = 0 if directions[directions_counter] == 'L' else 1
        current_node = _map[current_node][index]
        directions_counter = (directions_counter + 1) % len(directions)
    return steps

def navigate_map_ghost_style(_map: Dict[str, List[str]], directions: str):
    current_nodes = tuple(filter(lambda node: node.endswith('A'), _map.keys()))

    @lru_cache(maxsize=1024*2)
    def get_next_node(node: str, index: int) -> str:
        next_node = _map[node][index]
        return next_node

    def recurse(nodes: Tuple[str, str], directions_counter):
        index = 0 if directions[directions_counter] == 'L' else 1
        next_nodes = tuple(map(lambda node: get_next_node(node, index), nodes))
        if not all(next_node.endswith('Z') for next_node in next_nodes):
            directions_counter = (directions_counter + 1) % len(directions)
            print(directions_counter)
            return 1 + recurse(next_nodes, directions_counter)
        return 1
    result = recurse(current_nodes, 0)
    #print(recurse.cache_info())
    return result



def convert_map_to_lookup_structure(_map: List[str]) -> Dict[str, List[str]]:
    return {node: re.sub(r'[(),]', '', left_and_right_nodes).split() for node, left_and_right_nodes in map(lambda x: x.split(" = "), _map)}


if __name__ == "__main__":
    with open('input.txt') as fp:
        directions_and_map = list(filter(lambda s: s, map(str.strip, fp.readlines())))
        directions, *_map = directions_and_map
        _map = convert_map_to_lookup_structure(_map)
        if False:
            number_of_steps = navigate_map(_map, directions)
            print(number_of_steps)
        print(navigate_map_ghost_style(_map, directions))