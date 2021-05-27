#Python Hangman
#Author: Anthony Narlock
#Date: 12/30/2020
#Version: INDEVELOPMENT 0.4

import random

def get_word_list(difficulty):
    if(difficulty == "easy"):
        return [line.rstrip() for line in open("easy_word_list.txt")]
    elif(difficulty == "medium"):
        return [line.rstrip() for line in open("medium_word_list.txt")]
    elif(difficulty == "hard"):
        return [line.rstrip() for line in open("hard_word_list.txt")]
    else:
        print("An unexpected error occured when grabbing list information")

#generate_word: Generates randomly selected word from a list of words
def generate_word(word_list):
    return random.choice(word_list).lower()

#end_status: Displays the end status of the game (win/lose)
def end_status(word_guessed, lives, word):
    if(word_guessed == True):
        print("You win! The word was guessed.\nYou had " + str(lives) + " lives remaining.\n#############")
        again = input("play again? (y/n)")
        if(again == "y"):
            game()

    else:
        print("You lose! The word was: " + word + "\n#############")
        again = input("play again? (y/n)")
        if(again == "y"):
            game()

def main():
    print("Welcome to Hangman\nCreated by Anthony Narlock\n#############")
    game()

def game():
    print("Enter what difficulty you would like to play at:\nEasy: 3-5 letter words\nMedium: 6-9 letter words\nHard: 10+ letter words")
    difficulty = input("My difficulty: ")
    #while(difficulty.lower() != "easy" or difficulty.lower() != "medium" or difficulty.lower() != "hard"):
    #    print("Error: Expected difficulty response must be \"easy\", \"medium\", or \"hard\"")
    #    difficulty = input("My difficulty: ")

    #Read the file for the list of words
    word_list = get_word_list(difficulty)
    
    #Pick random word from the list
    word = generate_word(word_list)
    word_length = len(word)
    print("DEBUG: WORD=" + word)

    #Create pre-guessed word, which is hidden with dashes and
    #updated when the user correctly guesses a letter in the word
    dashed_word = '-' * word_length

    #Word has not been initially guessed, inital lives start at 6
    word_guessed = False
    letters_guessed = []
    lives = 6

    while(word_guessed == False):
        #Creates temporary dashed_word, to symbolize if a guess is
        #incorrect, lives will be deducted.
        temp_dashed_word = dashed_word

        #Creates a list, seperates specific "letters" for chosen
        dashed_word = list(dashed_word)
        guess = input("Guess: ")
        #If the guessed letter has already been entered, prompt user to re-enter until new is found
        while (guess in letters_guessed):
            print("You have already guessed that letter!")
            guess = input("Guess: ")

        #Add the newly guessed letter into the guessed letters list
        letters_guessed.append(guess)

        #Goes through dashes, changes to the letters if applicable
        for char in range(word_length):
            if (guess == word[char]):
                dashed_word[char] = guess

        #Joins the list back into a string
        dashed_word = "".join(dashed_word)
        print(dashed_word)

        if(dashed_word == word):
            word_guessed = True

        if(dashed_word == temp_dashed_word):
            lives = lives - 1
            #In the future, this would be where the GUI updates drawing hangman
            print("Incorrect guess! Lives remaining: " + str(lives))

        if(lives == 0):
            break
        #print("DEBUG:\ndashed_word = " + str(dashed_word) + "\nword = " + str(word) + "\nword_guessed = " + str(word_guessed))

    #The game of hangman is over, report end status
    end_status(word_guessed, lives, word)
    
if __name__ == "__main__":
    main()
