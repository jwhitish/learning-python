from string import ascii_letters, digits
import random
from random import choice



deck = ascii_letters[0:26]
#print(deck)

hand = ['a','b','c']

def hand_count(hand):
    count = 0
    for i in hand:
        count += 1
    while count < 6:
        hand2 = [random.choice(deck)]
        hand = hand + hand2
        count += 1
        print(hand)
        
    else:
        print(hand)





hand_count(hand)
