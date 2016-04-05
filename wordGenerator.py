import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHA = "abcdefghijklmnopqrstuvwxyz"
FORMAT = "abcdefghijklmnopqrstuvwxyz%#*"

word = ""
indiv_format = ""
word_format = ""

word_length = int(input("Enter length of word: "))

for i in range (1, word_length + 1):
    indiv_format = random.choice(FORMAT)
    word_format = word_format + indiv_format

for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(ALPHA)
    else:
        word += kind

print(word_format)
print(word)
