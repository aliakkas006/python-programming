# import cowsay
import sys
from random import choice, randint, shuffle
from statistics import mean

coin = choice(["heads", "tails"])
print(coin)

number = randint(1, 10)
print(number)

cards = ["king", "queen", "jack"]
shuffle(cards)

for card in cards:
    print(card)

mean_value = mean([40, 20])
print(mean_value)

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# cowsay.trex("My name is, " + sys.argv[1])
