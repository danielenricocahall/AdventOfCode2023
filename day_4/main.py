import re
from typing import List


def count_points_for_cards(cards: List[str]) -> int:
    return sum(map(count_points_for_card, cards))


def count_points_for_card(card: str) -> int:
    winning_numbers_we_have = compute_number_of_matches(card)
    if winning_numbers_we_have == 0:
        return 0
    return 2 ** (winning_numbers_we_have - 1)


def compute_scratch_cards_won(cards: List[str]) -> int:
    card_count = {k: 1 for k in range(1, len(cards) + 1)}
    for n, card in enumerate(cards, 1):
        number_of_matches = compute_number_of_matches(card)
        if number_of_matches > 0:
            for i in range(1, number_of_matches+1):
                card_count[n + i] += card_count[n]
    return sum(v for v in card_count.values())

def compute_number_of_matches(card: str) -> int:
    winning_numbers, numbers = card.split("|")
    winning_numbers = winning_numbers.split()
    numbers = numbers.split()
    matches = set(winning_numbers) & set(numbers)
    return len(matches)


if __name__ == "__main__":
    with open('./input.txt') as fp:
        cards = map(str.strip, fp.readlines())
        cards = map(lambda card: re.sub(r"Card\s\d+:\s", "", card), cards)
        cards = list(cards)
        total_points = count_points_for_cards(cards)
        total_scratch_cards_won = compute_scratch_cards_won(cards)
        print(total_points)
        print(total_scratch_cards_won)
