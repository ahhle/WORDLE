# CSCI 1550: HW 8, Problem 5
# Filename: hw8pr5.py
# Name: Ali Shlaibah
#
# Task: 5-letter word madness ... WORDLE!
import english_words as ew
wL_var = ew.english_words_set
import random

def extractWordleWords(word_list):
    """
    takes in word list
    if each word is 5 letters and doesnt start with a capital it appends it
    returns new list
    """
    newList = []
    for i in word_list:
        if len(i) == 5 and (i > "Z"):
            newList.append(i)
    return newList

def exactMatchLocs(word, guess):
    """
    takes two words
    goes through both word letter by letter to check if there are exact matches
    if there is, it stores the indicies of those matches and returns a list
    """
    exactMatchLetters = []
    for i in range(len(word)):
        if word[i] == guess[i]:
            exactMatchLetters.append(i)
    return exactMatchLetters

def maybeWeHave(letters, letter):
    """
    helper funciton that checks takes a letter and letters
    it returns true or false based of if the letter is inside the letters
    """
    return letter in letters

def partialMatchLocs(word, guess):
    """
    takes in two words, the real word and a guess
    goes through the word and guess - checks if we have a match on letters
        if we do - it checks if we already have those letters match and if it is not an exact match
            if all yes - then we add the index to a list!
                Finally it works!!!!!!!!!!!!!!!
    """
    partialMatchLetters = []
    for i in range(len(word)):
        for j in range(len(guess)):
            if guess[j] == word[i]:
                if not maybeWeHave(partialMatchLetters, j) and [i] != [j]: 
                    partialMatchLetters.append(j)
                    break
    return partialMatchLetters

def upperCase(myLetter):
    """
    takes a letter
    checks if it is already cappital
        if it is it return it back
    if its not it subtracts 32 from it and returns it, resulting in it being capital
    """
    if ord(myLetter) < 90:
        return myLetter
    return chr(ord(myLetter) - 32)

def wordleMatch(word, guess):
    if len(guess) != 5:
        return "Your guess is either too short or too long. Please make it 5 letters."
    """
    Takes in two words - findes their partial and exact matches
    returns new string
    """

    # was playing around after the assignmnt in and found out that the wordle doesnt do anything when i get it right
    # this fixes it
    if guess == word:
        return word

    newString = list("*****") # made it a list full of * so i dont have to worry about putting them
    exactMatches = exactMatchLocs(word, guess)
    partialMatches = partialMatchLocs(word, guess)

    # goes throught the partial matches and puts them in new string from guess
    for i in partialMatches:
        newString[i] = guess[i]

    # goes through the exact matches and uppercases them and puts them in their places
    for i in exactMatches:
        newString[i] = upperCase(guess[i])

    # makes the string one word then returns
    return ''.join(newString)



def myWordle():
    # get random word
    word = "poool" #random.choice(extractWordleWords(wL_var))
    i = 0
    while i in range(6):
        # get guess, print it, check if its right, if it is done
        guess = input("What is your guess?: ")
        result = wordleMatch(word, guess)
        print(result)
        i += 1
        if result == word:
            return print("Nice! you got it")
    print("Sorry, you have used all you guesses. Your punshiment now is never knowning the word. Cry about it.")
    print(word)

myWordle()