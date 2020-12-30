#Python Hangman
#Author: Anthony Narlock
#Date: 12/29/2020

import random

def main():
    #Read the file for the list of words
    get_lines = open("word_list.txt", "r").readlines()

    #Pick random word from the list
    word = random.choice(get_lines)
    word_length = len(word) - 1
    print("DEBUG: WORD=" + word)

    #Create pre-guessed word, which is hidden with dashes and
    #updated when the user correctly guesses a letter in the word
    dashed_word = '-' * word_length

    #Word has not been initially guessed, inital lives start at 6
    word_guessed = False
    lives = 6

    while(word_guessed == False):
        #Creates temporary dashed_word, to symbolize if a guess is
        #incorrect, lives will be deducted.
        temp_dashed_word = dashed_word

        #Creates a list, seperates specific "letters" for chosen
        dashed_word = list(dashed_word)
        guess = input("Guess: ")

        #Goes through dashes, changes to the letters if applicable
        for char in range(word_length):
            if (guess == word[char]):
                dashed_word[char] = guess

        #Joins the list back into a string
        dashed_word = "".join(dashed_word)
        print(dashed_word)

        if(str(dashed_word) == str(word)):
            word_guessed = True

        if(dashed_word == temp_dashed_word):
            lives = lives - 1
            print("Incorrect guess! Lives remaining: " + str(lives))

        if(lives == 0):
            break
        print("DEBUG:\ndashed_word = " + str(dashed_word) + "\nword = " + str(word) + "\nword_guessed = " + str(word_guessed))

    if(word_guessed == True):
        print("The word has been guessed!")
    else:
        print("You lose! The word was: " + word)
    


if __name__ == "__main__":
    main()
