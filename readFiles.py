from colorama import Fore, Back, Style
import random


def generation_random_words():
    file = open("Assets/Words.txt")
    readFile = file.read()
    splintWords = readFile.split(";")
    listWords = list(splintWords)
    randomizer = random.choice(listWords)
    return randomizer


print(generation_random_words())
