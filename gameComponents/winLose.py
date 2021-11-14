from gameComponents import gameVars


def winorlose(status):
    print("you " + status)

    choice = input("do you want to play again? y/n: ")

    if choice == "n":
        print(" !!!!!FINE!!!!! I didn't want to play again anyway...")
        exit()
    elif choice == "y":
        gameVars.playerLives = 3
        gameVars.computerLives = 3
        gameVars.player = False
