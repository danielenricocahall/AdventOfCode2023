from collections import Counter
from copy import copy
from dataclasses import dataclass
from enum import Enum, IntEnum
from itertools import product
from typing import List

LABEL_RANKS = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}


class HandType(IntEnum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


@dataclass
class Hand:
    cards: str
    hand_type: HandType
    bid: int

    def __lt__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        for card, other_card in zip(self.cards, other.cards):
            if card != other_card:
                return LABEL_RANKS[card] < LABEL_RANKS[other_card]

    def __eq__(self, other):
        return self.hand_type == other.hand_type and all(card == other_card for card, other_card in zip(self.cards, other.cards))

def compute_ranks(hands: List[str], bids: List[int], replace_jokers: bool = False) -> List[Hand]:
    hands = [Hand(cards=hand, hand_type=determine_hand_type(hand, replace_jokers), bid=bid) for bid, hand in zip(bids, hands)]
    ranked_hands = sorted(hands)
    return ranked_hands

def determine_hand_type(hand: str, replace_jokers: bool = False) -> HandType:
    num_distinct_cards = len(set(hand))
    counted_cards = Counter(hand)
    if replace_jokers:
        if n := counted_cards["J"]:
            all_hand_types = set()
            for combination in product(*n * [LABEL_RANKS.keys() - {"J"}]):
                hand_copy = copy(hand)
                for char in combination:
                    hand_copy = hand_copy.replace("J", char, 1)
                all_hand_types.add(determine_hand_type(hand_copy))
            return max(all_hand_types)
    # simple cases
    if num_distinct_cards == 1:
        return HandType.FIVE_OF_A_KIND
    elif num_distinct_cards == 5:
        return HandType.HIGH_CARD
    elif num_distinct_cards == 4:
        return HandType.ONE_PAIR
    counted_cards = Counter(hand)
    if len(counted_cards.keys()) == 3:
        # either two pair or three of a kind
        if any(v == 3 for v in counted_cards.values()):
            return HandType.THREE_OF_A_KIND
        return HandType.TWO_PAIR
    elif len(counted_cards.keys()) == 2:
        # either full house or four of a kind
        if any(v == 4 for v in counted_cards.values()):
            return HandType.FOUR_OF_A_KIND
        return HandType.FULL_HOUSE


def compute_total_winnings(ranked_hands: List[Hand]) -> int:
    return sum(i*hand.bid for i, hand in enumerate(ranked_hands, 1))


if __name__ == "__main__":
    with open('./input.txt') as fp:
        hands_and_bids = list(map(lambda s: s.strip().split(), fp.readlines()))
        hands, bids = zip(*hands_and_bids)
        bids = list(map(int, bids))
        ranked_hands = compute_ranks(hands, bids)
        #print(ranked_hands)
        print(compute_total_winnings(ranked_hands))
        # Part 2
        LABEL_RANKS.pop("J")
        LABEL_RANKS["J"] = 0
        ranked_hands_jokers_replaced = compute_ranks(hands, bids, replace_jokers=True)
        print(compute_total_winnings(ranked_hands_jokers_replaced))


