import random
from readFiles import generationRandomWords

randomWords = "SABER"
print(randomWords)

while True:
    testArray = []
    userResponse = input().upper()

    for i in range(5):
        if randomWords[i] == userResponse[i]:
            print(f"{userResponse[i]} - Posição correta")
            testArray.append(2)
        else:
            positionLetter = randomWords.find(userResponse[i])
            if positionLetter != -1:
                print(f"{userResponse[i]} - Existe, posição errada")
                testArray.append(1)
            else:
                print(f"{userResponse[i]} - Não existe")
                testArray.append(0)

    print(testArray)
    testArray = []

    if randomWords == userResponse:
        break
