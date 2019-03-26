from funzioniutili import readfile
from funzioniutili import colorprint
class World:
  def __init__(self,mappa):
    self.entities = []
    self.wallscoords = []
    self.doors = []
    self.mappa = mappa
    self.count = 0



  def add_entities(self, entities):
    self.entities += entities
  def getwallscoords(self):
    return self.wallscoords
  def getdoorscoords(self):
    return self.doors

  def draw(self):
    out = readfile(self.mappa)
    y = 0
    x = 0

    for cell in out:
        for e in self.entities:

            if e.x == x and e.y == y:
              colorprint(" G ")
              x += 1
              break
        else:
          if cell == "=":
            colorprint(" = ")
            self.wallscoords.append([x,y])
            x += 1
          elif cell == "#":
            colorprint("None")
            y += 1
            x = 0
          elif cell == "•":
            colorprint("   ")            
            x += 1
          elif cell == "-":
            if [x,y] in self.doors:
              colorprint(" - ")
            else:
              colorprint("   ")
            if self.count == 0:
              self.doors.append([x,y])
            x += 1
    self.count = 1



            

