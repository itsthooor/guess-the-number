#!/usr/bin/python3
import os
import random
import sys
import time


class globalVars():
    randomNumber = None
    userNumber = None


globalVar = globalVars()


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def correctNumberGuessed():
    clearConsole()
    print(
        f"Du hast es geschafft!\n
        Die gesuchte Nummer war tatsächlich {globalVar.userNumber}!")
    time.sleep(5)
    sys.exit()


if __name__ == "__main__":
    globalVar.randomNumber = random.choice(range(101))
    while globalVar.userNumber != globalVar.randomNumber:
        try:
            globalVar.userNumber = int(input("Rate die gesuchte Nummer: "))
            if globalVar.userNumber > globalVar.randomNumber:
                clearConsole()
                print(
                    f"Die gesuchte Zahl ist kleiner als {globalVar.userNumber}"
                    )
            elif globalVar.userNumber < globalVar.randomNumber:
                clearConsole()
                print(
                    f"Die gesuchte Zahl ist größer als {globalVar.userNumber}")
        except ValueError:
            clearConsole()
            pass
    correctNumberGuessed()
