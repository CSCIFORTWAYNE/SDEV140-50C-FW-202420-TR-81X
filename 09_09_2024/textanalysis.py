"""
Program: textanalysis.py
Author: Ken
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
"""

# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouyAEIOUY"
for word in text.split():
    #word.lower()
    wordSyllable = 0
    firstVowel = True
    for letter in word:
        if letter in vowels and firstVowel:
            wordSyllable += 1
            firstVowel = False
        else:
            firstVowel = True
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            wordSyllable -= 1
    if word.endswith('le'):
        wordSyllable += 1
    if wordSyllable == 0:
        syllables += 1
    else:
        syllables += wordSyllable

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")   

wordlist = text.split()
wordlist.sort()
print(wordlist)



