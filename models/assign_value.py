from itertools import combinations

# Define card ranks and values
RANKS = "23456789TJQKA"
VALUES = {rank: i for i, rank in enumerate(RANKS, start=2)}
SUITS = "CDHS"

# Define hand rankings with their base scores
HAND_RANKINGS = {
    "High Card": 0,
    "One Pair": 1000000,
    "Two Pair": 2000000,
    "Three of a Kind": 3000000,
    "Straight": 4000000,
    "Flush": 5000000,
    "Full House": 6000000,
    "Four of a Kind": 7000000,
    "Straight Flush": 8000000
}

def card_value(card):
    return VALUES[card[0]]

def card_suit(card):
    return card[1]

def is_straight(cards):
    values = sorted(set(card_value(card) for card in cards))
    if len(values) < 5:
        return False
    for i in range(len(values) - 4):
        if values[i:i+5] == list(range(values[i], values[i]+5)):
            return True
    return False

def is_flush(cards):
    suits = [card_suit(card) for card in cards]
    return any(suits.count(suit) >= 5 for suit in SUITS)

def classify_hand(hand, community_cards):
    all_cards = hand + community_cards
    all_combinations = list(combinations(all_cards, 5))
    
    best_hand = None
    best_hand_rank = -1
    best_score = 0

    for combo in all_combinations:
        rank_counts = {rank: 0 for rank in RANKS}
        for card in combo:
            rank_counts[card[0]] += 1

        if is_flush(combo) and is_straight(combo):
            hand_rank = "Straight Flush"
        elif 4 in rank_counts.values():
            hand_rank = "Four of a Kind"
        elif 3 in rank_counts.values() and 2 in rank_counts.values():
            hand_rank = "Full House"
        elif is_flush(combo):
            hand_rank = "Flush"
        elif is_straight(combo):
            hand_rank = "Straight"
        elif 3 in rank_counts.values():
            hand_rank = "Three of a Kind"
        elif list(rank_counts.values()).count(2) == 2:
            hand_rank = "Two Pair"
        elif 2 in rank_counts.values():
            hand_rank = "One Pair"
        else:
            hand_rank = "High Card"

        score = HAND_RANKINGS[hand_rank]
        score += sum(card_value(card) for card in combo)
        
        if score > best_score:
            best_score = score
            best_hand_rank = hand_rank
            best_hand = combo

    return best_score, best_hand_rank, best_hand

if __name__ == "__main__":
    hand = ["QH", "JC"]
    community_cards = ["JD", "JH", "JS", "2D", "3C"]

    score, hand_type, best_hand = classify_hand(hand, community_cards)
    print(f"Best hand: {best_hand}")
    print(f"Hand type: {hand_type}")
    print(f"Score: {score}")
