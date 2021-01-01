#Word Generator
#Author: Anthony Narlock
#Date: 12/30/2020

#Readme:
#The purpose of this Python script is to take a large list of words
#that was found via another GitHub link (see on next line)
#https://raw.githubusercontent.com/dwyl/english-words/master/words.txt
#and read and write to new files to create the words.
#I didn't want to write all of the words myself, so I thought I would have
#wrote a program to do it for me

word_list = [line.rstrip() for line in open("filtered.txt")]

easy_list = open("easy_word_list.txt", "a+")
medium_list = open("medium_word_list.txt", "a+")
hard_list = open("hard_word_list.txt", "a+")

for word in word_list:
    if (len(word) >= 3 and len(word) <= 5):
        easy_list.write(word + "\n")
    elif (len(word) >= 6 and len(word) <= 9):
        medium_list.write(word + "\n")
    elif (len(word) >= 10):
        hard_list.write(word + "\n")

print("Done")
easy_list.close()
medium_list.close()
hard_list.close()
word_list.close()
    
