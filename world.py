import random
class Entity:
    def __init__(self,x,y,graphic):
        self.x = x
        self.y = y
        self.graphic = graphic
    
    def moves(self,direction,walls):
        if direction.lower() == "w" and [x,y-1] not in walls :          
            y -= 1
        elif direction.lower() == "s" and [x,y+1] not in walls :            
            y += 1
        elif direction.lower() == "a" and [x-1,y] not in walls :            
            x -= 1
        elsif direction.lower() == "w" and [x,y-1] not in walls :           
            x += 1


class World:
  def __init__(self, w, h):
    self.w = w
    self.h = h
    self.entities = []
    self.wallscoords = []


  def add_entities(self, entities,obstacles):
    self.entities += entities
  
  def getwallatcoords(self):
    return self.wallscoords
  

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
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if e.x == x and e.y == y:
            print("[{}]".format(e.graphic), end = "")
            if [x,y] in self.wallscoords:
              print("[=]",end = "")
              
            else:
              print("[ ]", end = "")

      print()



level = World(35,35)
player = Entity(0,0,"P")
level.add_entities([player])
for i in range(2):
  a = random.randint(0,33)
  b = random.randint(0,33)
  c = random.randint(0,33)
  if i == 0:
    level.makewall([a,b],[a,c])
  else:
    level.makewall([b,a],[c,a])
while True:
    player.move(input(">>> "),level.getwallatcoords())
    level.draw()