import random
from os import system as cmd

with open('./words.txt') as wordRead:
    words = wordRead.readlines()

validInputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

index = random.randint(1, len(words))
word = words[index]
wordArray = []
for x in word:
    wordArray.extend(x)
wordArray.pop()
guesses = []
wrongGuesses = []
tries = 0
invalidInput = False
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


while (tries < 6):
    # clear terminal
    cmd('cls')

    # print the ASCII diagram
    print(hangmanVariants[tries])

    hiddenCount = 0
    # go through each letter, print it if its guessed right, otherwise print _
    for x in wordArray:
        if (guesses.__contains__(x)):
            print(x, end=' ')
        else:
            print('_', end=' ')
            hiddenCount += 1
    
    # print all the incorrect letters if the array is longer than 0
    if (len(wrongGuesses) > 0):
        print('\n \n [ ', *wrongGuesses, ' ] \n')
    else:
        print('\n \n \n')
    
    # ask for a letter
    if (invalidInput):
        print('Invalid input, punctuation and special characters not allowed!')
    guess = input('Guess a letter: ')
    
    if (validInputs.__contains__(guess) == False):
        invalidInput = True
        continue

    # if guessed right, add letter to guesses array; otherwise add to wrongGuesses and add 1 to tries
    if (word.__contains__(guess) == True):
        if (guesses.__contains__(guess) == False):
            guesses.append(guess)
        invalidInput = False
    else:
        if (wrongGuesses.__contains__(guess) == False):
            wrongGuesses.append(guess)
            tries += 1
        invalidInput = False
    
    # if tries is at 6, cleas terminal and print final ASCII diagram with losing text
    if (tries == 6):
        cmd('cls')
        print(hangmanVariants[tries])
        print(f'You lost... The word was: {word}')
        exit()

    # winning message when guessing all the letters!
    if (hiddenCount == 0):
        cmd('cls')
        print(hangmanVariants[tries])
        print(*wordArray)
        print('\n ⁂ You won!!! ⁂')
