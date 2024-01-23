#scrip que genere el lan de dos dados
from random import randint


dice1 = randint(1, 6)
dice2 = randint(1, 6)

def areEqual(dice1, dice2):
    print("dice 1: ", dice1)
    print("dice 2: ", dice2)
    if dice1 == dice2:
        print("Ganaste")
    else:
        print("Perdiste")


areEqual(dice1, dice2)