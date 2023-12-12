from typing import List

def process_environmental_report(report: List[List[int]], backwards: bool = False):
    if backwards:
        extrapolate = extrapolate_first_value
    else:
        extrapolate = extrapolate_next_value
    return sum(map(extrapolate, report))

def extrapolate_next_value(sequence: List[int]) -> int:
    current_sequence = sequence
    last_values = []
    while not all(x == 0 for x in current_sequence):
        last_values.append(current_sequence[-1])
        current_sequence = [y - x for (x, y) in zip(current_sequence, current_sequence[1:])]
    return sum(last_values)

def extrapolate_first_value(sequence: List[int]) -> int:
    return extrapolate_next_value(list(reversed(sequence)))



if __name__ == "__main__":
    with open('input.txt') as fp:
        report = map(str.strip, fp.readlines())

        report = list(map(lambda seq: list(map(int, seq.split(" "))), report))
        print(process_environmental_report(report))
        print(process_environmental_report(report, backwards=True))


