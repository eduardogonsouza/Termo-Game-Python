from colorama import Fore, Back, Style
import random


def generationRandomWords():
    file = open("Assets/Words.txt")
    readFile = file.read()
    splintWords = readFile.split(";")
    listWords = list(splintWords)
    randomizer = random.choice(listWords)
    return randomizer
