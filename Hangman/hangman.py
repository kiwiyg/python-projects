import random
from wordslist import words
from hangmanVisual import lives_visual_dict
import string

def get_word(words):
    word = random.choice(words)
    while '-' in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word= get_word(words)
    wordletters= set(word)
    alphabet= set(string.ascii_uppercase)
    usedletters= set()


    lives = 7


    while len(wordletters)>0 and lives>0:
        print("\nYou have ", lives, " lives left and you have used these letters: ", " ".join(usedletters))

        word_list = [letter if letter in usedletters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))
        
        usedletter= input("\nGuess a letter: ").upper()

        if usedletter in alphabet- usedletters:
            usedletters.add(usedletter)
            if usedletter in wordletters:
                wordletters.remove(usedletter)
                print(' ')
            else:
                lives= lives-1
                print("Your letter ", usedletter, " is not in the word.")

        elif usedletter in usedletters:
            print("\n You have already used that letter, choose another letter.")
        else:
            print("\nThat is an invalid input. You can only enter alphabets.")
    if lives==0:
        print(lives_visual_dict[lives])
        print("You died. Better luck next time.\nThe word was ", word)
    else:
        print("Yay to you! You guessed it :) The word is ", word)
        


print("Welcome to the HangMan. \nYou will now have to guess letters of a random word from our list. \nBest of Luck!")
o=1
while o==1:
    hangman()
    o=int(input("Do you want to go for another round? \nEnter 1 for Yes and 0 for No\n"))

print("Farewell ~~")