import random

with open('./words.txt') as wordRead:
    words = wordRead.readlines()

index = random.randint(1, len(words))
word = words[index]
guesses = []
hangmanVariants = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
tries = 0
while (tries < 6):
    print(hangmanVariants[tries])
    print('_ ' * len(word))
    guess = input('Guess a letter: ')
    if(word.find(guess)):
        print('word contains the letter')
        exit()

    if (tries == 6):
        print(hangmanVariants[tries])
        print('You lost...')
        exit()
