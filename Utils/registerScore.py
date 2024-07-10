import time, sys, os

sys.path.insert(0, os.path.abspath(""))
from InquirerPy import inquirer
from Utils.utilsVariables import terminalSize


def registerScorePlayer(playerName, attempts, elapsedTime):
    with open("Assets\score.txt", "r") as arq:
        dataStorage = arq.readlines()

    storesPlayers = []
    storesNumbersAttemps = []
    storesTimes = []

    for line in dataStorage:
        part = line.split(";")
        storesPlayers.append(part[0])
        storesNumbersAttemps.append(int(part[1]))
        storesTimes.append(float(part[2]))

    storeTogether = zip(storesPlayers, storesNumbersAttemps, storesTimes)
    currentStorePlayer, currentStoreAttemp, currentStoreTime = zip(*storeTogether)

    with open("Assets\score.txt", "w") as arq:
        for storePlayer, storeAttemp, storeTime in zip(
            currentStorePlayer, currentStoreAttemp, currentStoreTime
        ):
            arq.write(f"{storePlayer};{storeAttemp};{storeTime}\n")
        arq.write(f"{playerName};{attempts};{elapsedTime}\n")


def rankingScore():
    if os.path.isfile("Assets\score.txt"):
        with open("Assets\score.txt", "r") as arq:
            dataScore = arq.readlines()
    else:
        dataScore = []

    player = []
    numberAttemp = []
    time = []

    for line in dataScore:
        part = line.split(";")
        player.append(part[0])
        numberAttemp.append(int(part[1]))
        time.append(float(part[2]))

    together = sorted(zip(player, numberAttemp, time))
    currentPlayer, currentNumberAttemp, currentTime = zip(*together)

    print("\nPosição    Nome do Jogador...:                  Tentativas......:")
    print("-" * terminalSize)

    for num, (namePlayer, attempNumber, segundsTime) in enumerate(
        zip(currentPlayer, currentNumberAttemp, currentTime), start=1
    ):
        print(
            f"{num}          Nome do Jogador: {namePlayer:10s}          Número de Tentativas: {attempNumber}          Tempo em Segundos: {segundsTime:.2f} Segundos"
        )

    isReturn = inquirer.confirm(message="<- Retornar").execute()
    if isReturn == False:
        exit()
