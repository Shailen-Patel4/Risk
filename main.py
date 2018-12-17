import numpy
from matplotlib import pyplot as plt




def roll():
    return np.random.randint(1,6)

class player(object):
    """docstring for player."""
    def __init__(self, name, units, roll):
        self.name = name
        self.units = units
        self.roll = roll
number_of_players = int(input("how many players?"))
player_template = "Player %d"
players=[]
for i in range(1,number_of_players+1):
    players.append(input(player_template%(i)+": "))
print(players)
end = 0
while end == 0:
    attacker = player(players[int(input("Attacker: "))-1], int(input("Units: ")))
    defender = player(players[int(input("Defender: "))-1], int(input("Units: ")))

    end == int(input("End? "))
# what else to add?
