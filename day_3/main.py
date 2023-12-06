import re


def analyze_schematic(engine_schematic):
    row_to_nums = {row_num: re.findall(r'\d+', row) for row_num, row in enumerate(engine_schematic)}
    part_numbers = []
    for i in range(len(engine_schematic)):
        for num in row_to_nums[i]:
            index = engine_schematic[i].index(num)
            neighbors = []
            if index > 0:
                left_neighbor = engine_schematic[i][index - 1]
                neighbors.append(left_neighbor)
            if index + len(num) < len(engine_schematic[i]):
                right_neighbor = engine_schematic[i][index + len(num)]
                neighbors.append(right_neighbor)
            if i + 1 < len(engine_schematic):
                bottom_neighbors = engine_schematic[i + 1][max(index-1, 0):index+len(num)+1]
                neighbors.extend(bottom_neighbors)
            if i > 0:
                top_neighbors = engine_schematic[i - 1][max(index-1, 0):index+len(num)+1]
                neighbors.extend(top_neighbors)
            if not all(x == '.' for x in neighbors):
                part_numbers.append(num)
            else:
                print(f"{num} is not a part number: {neighbors}")
            print(num, neighbors)
    print(part_numbers)
    return sum(map(int, part_numbers))


if __name__ == "__main__":
    with open('./test.txt', 'r') as fp:
        engine_schematic = list(map(str.strip, fp.readlines()))
        print(engine_schematic)
        print( analyze_schematic(engine_schematic)) # 553079