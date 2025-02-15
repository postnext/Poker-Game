
import random

RANKS = "23456789TJQKA"
SUITS = "CDHS"

deck = [r + s for r in RANKS for s in SUITS]
random.shuffle(deck)

your_hand = deck[:5]
dealer_hand = deck[5:10]

print("Your hand:", your_hand)
print("Dealer's hand:", dealer_hand)

your_score = sum(RANKS.index(card[0]) for card in your_hand)
dealer_score = sum(RANKS.index(card[0]) for card in dealer_hand)

if your_score > dealer_score:
    print("🎉 Ви виграли!")
elif your_score < dealer_score:
    print("😢 Ви програли!")
else:
    print("🤝 Нічия!")
