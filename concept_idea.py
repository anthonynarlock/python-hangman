#Original Concept - Guess Word
#Author: Anthony Narlock
#Date: 12/05/2020

#Main function
def main():
    #Select a word (in future from a file, will pick word randomly)
    word = "abandoned"
    word_length = len(word)

    #Creates dummy "dashed-word, which is the amount of chars in the
    #word, but uses dashes.
    dashed_word = '-' * len(word)

    word_guessed = False

    while(word_guessed == False):
        #Creates a list, seperates specific "letters" for chosen
        dashed_word = list(dashed_word)
        guess = input("Guess: ")

        #Goes through dashes, changes to the letters if applicable
        for char in range(word_length):
            if(guess == word[char]):
                dashed_word[char] = guess

        #Joins the list back into a string
        dashed_word = "".join(dashed_word)
        print(dashed_word)
        if(dashed_word == word):
            word_guessed = True

    print("The word has been guessed!")

#Call the main function
if __name__ == "__main__":
    main()
