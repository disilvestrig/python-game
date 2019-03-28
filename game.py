import os
from world import World
from entity import Entity
from info import info
level = World("./stanza1.txt")
lista = info
player = Entity(4,4,"G",[ ])
x1 = int(lista.entity["E"]["x"])
y1 = int(lista.entity["E"]["y"])
x2 = int(lista.entity["$"]["x"])
y2 = int(lista.entity["$"]["y"])
e = Entity(x1,y1,"E",[ ])
s = Entity(x2,y2,"$",[ ])
level.add_entities([player,e,s])

while True:
  level.draw()
  player.printinventory()
  a = input(">>> ")
  if a.lower() == "o":
    level.doors.remove(player.opendoor(level.getdoorscoords()))
  if a.lower() == "e":
    print(lista.entity["interaction"]["e"])
    input()
  if a.lower() == "e$" and s in player.getinventory():
    print(lista.entity["interaction"]["e$"])
    input()
  if a.lower() == "$":
    print(lista.entity["interaction"]["$"])
    player.putininventory(s)
    level.add_entities([player,e])

  else:
    player.move(a.lower(),level.getwallscoords(),level.getdoorscoords())
  os.system("clear")
  