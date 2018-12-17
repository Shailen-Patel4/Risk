import pandas as pd
import numpy as np

def rolldice(defender, attacker):
    defender_dice = []
    attacker_dice = []
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
    return defender_dice, attacker_dice


# def matchingdice(defender_dice, attacker_dice):
#     defencewins = []
#     sorted(defender_dice, reverse = True)
#     sorted(attacker_dice)
#     if attacker_dice[0] < defender_dice[0]:
#         defencewins.append(1)
#     else:
#         defencewins.append(0)
#     if attacker_dice[1] < defender_dice[1]:
#         defencewins.append(1)
#     else:
#         defencewins.append(0)
#     if attacker_dice[3] < defender_dice[1]:

[x, y] = rolldice(2,3)
print(sorted(x, reverse = True), sorted(y, reverse = True))
# defenders_dice = for
# sorted(y)
# print(y)
# print(y[0])
