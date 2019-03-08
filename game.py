import os
from world import World
from entity import Entity
level = World("./stanza1.txt")
player = Entity(6,5,"G")
level.add_entities([player])
while True:
  level.draw()
  player.move(input(">>> "),level.getwallscoords())
  os.system("clear")
  