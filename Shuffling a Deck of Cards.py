import itertools
import random

deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))
random.shuffle(deck)

print("Your combination of cards is: ")

for i in range(11):
    print(deck[i][0], "of", deck[i][1])
