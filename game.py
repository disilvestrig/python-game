import os
from world import World
from entity import Entity
level = World("./stanza1.txt")
player = Entity(4,4,"G")
level.add_entities([player])
while True:
  level.draw()
  a = input(">>> ")
  if a.lower() == "o":
  	level.doors.remove(player.opendoor(level.getdoorscoords()))
  else:
    player.move(a.lower(),level.getwallscoords(),level.getdoorscoords())
  os.system("clear")
  