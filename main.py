from random import randint
from gameComponents import winLose, gameVars, gameResult

print("***ROCK***PAPER***SCISSORS***")
print("choose wisely...")

while gameVars.player is False:
    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    gameResult.winnerResult()

    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost </3")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won <3333")

    gameVars.player = False
