import json
from info import info
lista = info()

class Entity:
  def __init__(self,x,y,graphic,inventory):
    self.x = x
    self.y = y
    self.graphic = graphic
    self.inventory = [ ]
  def move(self,direction,wall,door):
    x = self.x
    y = self.y
    if direction.lower() == "w" and [x,y-1] not in wall and [x,y-1] not in door  :
      self.y -= 1
    elif direction.lower() == "s" and [x,y+1] not in wall and [x,y+1] not in door :
      self.y += 1
    elif direction.lower() == "a" and [x-1,y] not in wall and [x-1,y] not in door :
      self.x -= 1
    elif direction.lower() == "d" and [x+1,y] not in wall and [x+1,y] not in door :
      self.x += 1
  def putininventory(self,obj):
  	self.inventory.append(obj)
  	return self.inventory
  def getinventory(self):
  	return self.inventory
  def printinventory(self):
  	for e in self.inventory:
  		print(lista.entity[e.graphic]["nome"],":",lista.entity[e.graphic]["description"])

  def opendoor(self,door):
    ray = []
    ray.append([self.x,self.y-1])
    ray.append([self.x,self.y+1])
    ray.append([self.x-1,self.y])
    ray.append([self.x+1,self.y])
    for i in ray:
      if i in door:
        return i






