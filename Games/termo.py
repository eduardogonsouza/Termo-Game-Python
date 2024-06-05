import time
from Utils.InputLimited import inputLimited
from Utils.utilsCode import CLEAR_RIGHT, PREV_LINE, terminalSize
from termcolor import colored


def gameTermo(randomWords):
    countAttempt = 1
    while True:
        attempt = ""

        userAnswer = inputLimited(5, terminalSize)

        time.sleep(1)

        print(PREV_LINE, CLEAR_RIGHT)

        dividedAnswer = list(userAnswer)

        loading = ""

        for i in range(len(dividedAnswer)):

            loading = loading + dividedAnswer[i].replace(dividedAnswer[i], "⬜")

            print(f"{PREV_LINE}{loading.center(terminalSize)}")

            time.sleep(0.3)

            print(PREV_LINE, CLEAR_RIGHT)

            positionLetter = randomWords.find(userAnswer[i])
            if randomWords[i] == userAnswer[i]:

                attempt += colored(dividedAnswer[i], "green")

            elif positionLetter != -1:
                attempt += colored(dividedAnswer[i], "yellow")
            else:
                attempt += colored(dividedAnswer[i], "red")

        time.sleep(0.5)

        print(PREV_LINE, CLEAR_RIGHT)

        time.sleep(0.5)
        print(f"{PREV_LINE}{attempt.center(terminalSize + 43 )}")

        if randomWords == userAnswer or countAttempt >= 5:
            break
        else:
            countAttempt += 1
