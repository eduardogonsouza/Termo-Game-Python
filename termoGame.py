from colorama import Fore, Back, Style
import random

file = open("Assets/Words.txt")
readFile = file.read()
splintWords = readFile.split(",")
listWords = list(splintWords)
file.close()

randomizer = random.choice(listWords)
randomizerWord = list(randomizer)
print(Back.GREEN + randomizerWord[0])
