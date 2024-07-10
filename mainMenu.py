import os
from Games.termo import gameTermo
from Utils.utilsVariables import terminalSize
from Utils.readFiles import generationRandomWords
from Utils.registerScore import rankingScore
from InquirerPy import inquirer
from InquirerPy.base.control import Choice


currentRandomWord = generationRandomWords()

while True:
    os.system("cls")

    print(
        ",--------.   ,------.   ,------.    ,--.   ,--.    ,-----. ".center(
            terminalSize
        )
    )
    print(
        "'--.  .--'   |  .---'   |  .--. '   |   `.'   |   '  .-.  ' ".center(
            terminalSize
        )
    )
    print(
        "   |  |      |  `--,    |  '--'.'   |  |'.'|  |   |  | |  | ".center(
            terminalSize
        )
    )
    print(
        "   |  |      |  `---.   |  | |  |   |  |   |  |   '  '-'  ' ".center(
            terminalSize
        )
    )
    print(
        "   `--'      `------'   `--' '--'   `--'   `--'    `-----' ".center(
            terminalSize
        )
    )

    selectMenu = inquirer.select(
        message="",
        choices=[
            Choice(value=1, name="Jogar".center(terminalSize)),
            Choice(value=2, name="Pontuação Local".center(terminalSize)),
            Choice(value=3, name=" Exit ".center(terminalSize)),
        ],
        default=None,
    ).execute()

    if selectMenu == 1:
        gameTermo(currentRandomWord)
    elif selectMenu == 2:
        rankingScore()
    else:
        exit()
