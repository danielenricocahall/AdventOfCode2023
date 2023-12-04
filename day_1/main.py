import re
from typing import List

digit_name_to_value_mapping = {'one': '1', 'two': '2', 'three': '3',
                               'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
REGEX_PATTERN = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')


def calibrate_document(lines: List[str]) -> int:
    total_sum = 0
    for line in lines:
        groups = REGEX_PATTERN.findall(line)
        digits = [digit_name_to_value_mapping.get(match, match) for match in groups]
        print(digits)
        if len(digits) == 1:
            digits *= 2
        first_digit, last_digit = digits[0], digits[-1]
        print(first_digit + last_digit)
        total_sum += int(first_digit + last_digit)
    return total_sum


if __name__ == "__main__":
    with open('./input.txt') as fp:
        lines = list(map(str.strip, fp.readlines()))
    print(calibrate_document(lines))
