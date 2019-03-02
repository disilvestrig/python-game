import random 
import os


class Entity:
  def __init__(self,x,y,graphic,):
    self.x = x
    self.y = y
    self.graphic = graphic
  def move(self,direction,wall,field):
    x = self.x
    y = self.y
    if direction.lower() == "w" and [x,y-1] not in wall and [x,y-1] in field:
      self.y -= 1
    elif direction.lower() == "s" and [x,y+1] not in wall and [x,y+1] in field:
      self.y += 1
    elif direction.lower() == "a" and [x-1,y] not in wall and [x-1,y] in field:
      self.x -= 1
    elif direction.lower() == "d" and [x+1,y] not in wall and [x+1,y] in field:
      self.x += 1
    elif direction.lower() == "q":
        return


class World:
  def __init__(self, w, h):
    self.w = w
    self.h = h
    self.entities = []
    self.wallscoords = []
    self.field = []


  def add_entities(self, entities):
    self.entities += entities
  def getwallscoords(self):
    return self.wallscoords
  def getdimension(self):
    for i in range(self.h):
        for g in range(self.w):
            self.field.append([g,i])
    return self.field
  

  def makewall(self,exa,exb):
    if exa[0] == exb[0]:
      if exa[1] - exb[1] > 0:
        a = exb[1]
        while a < exa[1]:
          self.wallscoords.append([exa[1],a])
          a += 1
      elif exa[1] - exb[1] < 0:
        a = exa[1]
        while a < exb[1]:
          self.wallscoords.append([a,exb[1]])
          a += 1
    elif exa[1] == exb[1]:
      if exa[0] - exb[0] > 0:
        a = exb[0]
        while a < exa[0]:
          self.wallscoords.append([exa[0],a])
          a += 1
      elif exa[0] - exb[0] < 0:
        a = exa[0]
        while a < exb[0]:
          self.wallscoords.append([a,exb[0]])
          a += 1




  def draw(self):
    p = self.entities[0]
    view = []
    a = -2
    b = -2
    for i in range (5):

      for g in range(6):
        view.append([p.x+a,p.y+b])
        b += 1
        if b > 2:
            b = -2
      a += 1
    view.remove([p.x,p.y])


    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if p.x == x and p.y == y:
            print("[{}]".format(e.graphic), end = "")
            break
        else:    
          if [x,y] in view and [x,y] in self.wallscoords:
            print("[=]", end = "")
          elif [x,y] in view:
            print("[ ]", end = "")
          else:
            print(" • ", end = "")
      print()




player = Entity(0,0,"G")
level = World(35,35)
level.add_entities([player])

for i in range(random.randint(0,10)):  
  a = random.randint(0,33)
  b = random.randint(0,33)
  c = random.randint(0,33)
  while [a,b] == [0,0] and [a,c] == [0,0]:
    a = random.randint(0,33)
    b = random.randint(0,33)
    c = random.randint(0,33)
  if i % 2 == 0:
    level.makewall([a,b],[a,c])
  else:
    level.makewall([b,a],[c,a])
while True:
  level.draw()
  player.move(input(">>> "),level.getwallscoords(),level.getdimension())
  os.system("clear")