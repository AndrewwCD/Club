import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
class Club:
    def __init__(self,club_name):
        self.players = []
        self.coaches = []
        self.managers = []
        self.club_name = club_name
    def add_player(self,name,number,position,nation):
        player = {"name" : name, "number" : number, "position" : position, "nation" : nation}
        self.players.append(player)
    def remove_player(self,position):
        self.players.pop(position)
    def add_coach(self,name,position):
        coach = {"name" : name, "position" : position}
        self.coaches.append(coach)
    def remove_coach(self,position):
        self.coaches.pop(position)
    def add_manager(self,name,position):
        manager = {"name" : name, "position" : position}
        self.managers.append(manager)
    def remove_manager(self,position):
        self.managers.pop(position)

_Manchester_City = Club("Manchester City")
print(_Manchester_City.club_name)
_Manchester_City.add_player("Kyle walker", 2, "DF", "ENG")
_Manchester_City.add_player("Rúben Dias", 3, "DF", "POR")
_Manchester_City.add_player("John Stones", 5, "DF", "ENG")
_Manchester_City.add_player("İlkay Gündoğan", 8, "MF", "GER")
_Manchester_City.add_coach("Pep Guardiola","Head Coach")
_Manchester_City.add_coach("Juan Manuel Lillo","Assistant Coach")
_Manchester_City.add_coach("Brian Kidd","Assistant Coach")
_Manchester_City.add_manager("Enzo Maresca","Under-23 EDS manager")
_Manchester_City.add_manager("Carlos Vicens","Under-18 Academy Team Manager")

print("players \n", _Manchester_City.players)
_Manchester_City.remove_player(1)
print("players \n", _Manchester_City.players)
print("coaches \n", _Manchester_City.coaches)
_Manchester_City.remove_coach(2)
print("coaches \n", _Manchester_City.coaches)
print("managers \n", _Manchester_City.managers)
_Manchester_City.remove_manager(0)
print("managers \n", _Manchester_City.managers)

fig,ax = plt.subplots()
opposing_team = ["Port Vale","Fulham","Sheffield Wednesday","Newcastle United","Arsenal"]
manchester_score = [4,4,1,2,0]
opposing_score = [1,0,0,0,2]
width = 0.35
x = np.arange(len(opposing_team))
ax.bar(x - width/2, manchester_score, width, label='Manchester City')
ax.bar(x + width/2, opposing_score, width, label='Opposing Team')
ax.set_ylabel("Scores")
ax.set_xlabel("Opposing Team")
ax.set_title("2019–20 FA Cup")
ax.set_xticks(x)
ax.set_xticklabels(opposing_team,rotation = 45)
ax.legend()
fig.tight_layout()
plt.show()