import time, sys, os

sys.path.insert(0, os.path.abspath("Utils"))
from InputLimited import inputLimited
from utilsVariables import CLEAR_RIGHT, PREV_LINE, terminalSize
from registerScore import registerScorePlayer
from readFiles import generationRandomWords
from termcolor import colored, cprint
from InquirerPy import inquirer


def thanksForPlaying(continueGame, playerName, attempts, time):
    newRandomWord = generationRandomWords()
    if continueGame == True:
        registerScorePlayer(playerName, attempts, time)
        gameTermo(newRandomWord)
    else:
        print("\n")
        cprint(
            f"Muito Obrigado!! Por jogar!!".center(terminalSize),
            attrs=["bold"],
        )
        registerScorePlayer(playerName, attempts, time)
        exit()


def currentContinueGame():
    return inquirer.confirm(message="Deseja Tentar Novamente ?").execute()


def gameTermo(RandomWords):
    os.system("cls")

    currentPlayerName = input("Digite seu Nome: ")

    os.system("cls")

    cprint("Escreva Uma Palavra de....".center(terminalSize), attrs=["bold"])
    cprint("5 Letras".center(terminalSize), "cyan")
    print("\n")
    cprint("Você tem 5 Tentativas".center(terminalSize), attrs=["bold"])
    print("-" * terminalSize)
    print("\n")

    # print(RandomWords)

    startTime = time.time()

    print("Palavra".center(terminalSize), flush=True, end="")
    print("\rNº Da Tentativa", flush=True)

    numberAttempt = 1
    wishContinueGame = True
    while True:
        attempt = ""

        userAnswer = inputLimited(5, terminalSize)

        time.sleep(1)

        print(PREV_LINE, CLEAR_RIGHT)

        dividedAnswer = list(userAnswer)

        loading = ""
        for i in range(len(dividedAnswer)):
            loading = loading + dividedAnswer[i].replace(dividedAnswer[i], "⬜")

            print(f"{PREV_LINE}{CLEAR_RIGHT}{loading.center(terminalSize - 5)}")
            time.sleep(0.3)
            positionLetter = RandomWords.find(userAnswer[i])

            if RandomWords[i] == userAnswer[i]:
                attempt += colored(dividedAnswer[i], "green")
            elif positionLetter != -1:
                attempt += colored(dividedAnswer[i], "yellow")
            else:
                attempt += colored(dividedAnswer[i], "red")

        time.sleep(0.5)

        print(PREV_LINE, CLEAR_RIGHT)

        time.sleep(0.5)
        print(f"{PREV_LINE}{attempt.center(terminalSize + 43)}")
        cprint(f"{PREV_LINE}{numberAttempt}", attrs=["bold"])

        if RandomWords == userAnswer or numberAttempt >= 8:
            endTime = time.time()
            if RandomWords == userAnswer:
                cprint(
                    "Parabens você acertou!!".center(terminalSize),
                    "green",
                    attrs=["bold"],
                )

                wishContinueGame = currentContinueGame()

                thanksForPlaying(
                    wishContinueGame,
                    currentPlayerName,
                    numberAttempt,
                    time=(endTime - startTime),
                )

            else:
                print(
                    "Ops!! Você gastou todas as tentativas a palavra correta era:".center(
                        terminalSize
                    )
                )
                cprint(f"{RandomWords}".center(terminalSize), "red", attrs=["bold"])

                wishContinueGame = currentContinueGame()

                thanksForPlaying(
                    wishContinueGame,
                    currentPlayerName,
                    numberAttempt,
                    time=(endTime - startTime),
                )

        else:
            numberAttempt += 1
