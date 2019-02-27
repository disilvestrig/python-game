import random
class World:
  def __init__(self, w, h):
    self.w = w
    self.h = h
    self.entities = []
    self.wallscoords = []


  def add_entities(self, entities,obstacles):
    self.entities += entities
  

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
#        for e in self.entities:
#          if e.x == x and e.y == y:
#            print("[{}]".format(e.graphic), end = "")
            if [x,y] in self.wallscoords:
              print("[=]",end = "")
              
            else:
              print("[ ]", end = "")

      print()




#level.add_entities([player, monster])
#level = World(20,20)
#for i in range(2):
#  a = random.randint(0,20)
#  b = random.randint(0,20)
#  c = random.randint(0,20)
#  if i == 0:
#    level.makewall([a,b],[a,c])
#  else:
#    level.makewall([b,a],[c,a])

level.draw()