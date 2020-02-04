import cards

hand_size = 5
num_players = 4
hands = []

deck = cards.Deck() ## accessing a class within a module
deck.shuffle()

for i in range(num_players):
    hands.append(deck.deal_hand(hand_size))

print()
print("Cards Version", cards.VERSION)  ## accessing a variable within a module
for h in hands:
    print()
    cards.print_hand(h)  ## accessing a function within a module
print()

