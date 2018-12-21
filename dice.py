import pandas as pd
import numpy as np

def rolldice(attacker, defender):
    defender_dice = []
    attacker_dice = []
    determinator = []
    for i in range(0, defender):
        x = np.random.randint(1,7)
        defender_dice.append(x)
    for i in range(0,3-defender):
        defender_dice.append(0)
    for i in range(0, attacker):
        x = np.random.randint(1,7)
        attacker_dice.append(x)
    for i in range(0,3-attacker):
        at_dice.append(0)
    defender_dice.sort(reverse=True)
    attacker_dice.sort(reverse=True)
    for i in range(0, len(attacker_dice)):
        determinator.append(attacker_dice[i]-defender_dice[i])
    return attacker_dice, defender_dice, determinator

[x, y, result] = rolldice(3,2)
print(x,y, result)
