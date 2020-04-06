#!/usr/bin/env python3

#Use of arguments list
from sys import argv
#Use of pre-generated list of each letter on the alphabet
from string import ascii_lowercase as alphabet

#Parse the dictionnary
def parseDict():
    #Use of 'with' automatically close the file
    with open("words_alpha.txt", "r") as input_file:
        #Split each line and add it to the set. Set is used here to access a file in O(1). Frozen means it is not mutable
        dictionnary = frozenset(word for word in input_file.read().split('\n'))
    return dictionnary

def generateCorrections(word):
    #Generate subset of the word
    split = [(word[:i], word[i:]) for i in range(len(word) + 1)]

    #Generate all corrections by removing each letter once
    remove = [left + right[1:] for left, right in split if right]
    #Add more corrections by inserting each letter of the alphabet at every position once
    insert = [left + middle + right for left, right in split for middle in alphabet]
    #Add even more corrections by replacing each letter by every letter of the alphabet once
    replace = [left + middle + right[1:] for left, right in split if right for middle in alphabet]
    #Add further corrections by switching each letter once
    switch = [left[:-1] + right[0] + left[-1] + right[1:] for left, right in split if right and left]

    #Merge all corrections
    return set(remove + insert + replace + switch)

def autocorrect(dictionnary, word):
    #Check if the word is already valid
    if word in dictionnary:
        return word
    #Return all valid words found in corrections
    return set(word for word in generateCorrections(word) if word in dictionnary)

if __name__ == '__main__':
    #Generate dictionnary
    if (len(argv) < 2):
        print("Please provide a word as argument.")
    #Apply algorithm
    else:
        dictionnary = parseDict()
        corrected = autocorrect(dictionnary, argv[1])
        print(corrected if len(corrected) else "No correction has been found.")

#Down below are updated functions to add word frequency, just replace the old one to make them work
# def parseDict():
#     with open("frequency.txt", "r") as input_file:
#         #Use of dictionnary to keep the record of each word frequency rank (order of appearance in the file)
#         dictionnary = dict((word, i) for i, word in enumerate(input_file.read().split('\n')))
#     return dictionnary

# def autocorrect(dictionnary, word):
#     #Check if the word is already valid
#     if word in dictionnary:
#         return word
#     #Find all valid words found in corrections
#     valid = dict((word, dictionnary[word]) for word in generateCorrections(word) if word in dictionnary.keys())
#     #Return the most frequent one
#     return min(valid, key=valid.get)