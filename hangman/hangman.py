import random
from os import system as cmd

with open('./words.txt') as wordread:
   words = wordread.readlines()

word = random.choice(words)
word = word.strip()
print(word)
print('_' * len(word))
attempts = 0
letters = []
wrongLetters = []