from readFiles import generationRandomWords
from Utils.InputLimited import inputLimited
from Utils.utilsCode import CLEAR_RIGHT, PREV_LINE, terminalSize
from Games.termo import gameTermo
from termcolor import colored
import os, time

randomWords = generationRandomWords()

os.system("cls")


print("Digite uma palavra com 5 Letras")
print(randomWords)


countAttempt = 1

gameTermo(randomWords)
