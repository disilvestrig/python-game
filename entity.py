class Entity:
  def __init__(self,x,y,graphic):
    self.x = x
    self.y = y
    self.graphic = graphic
  def move(self,direction,wall):
    x = self.x
    y = self.y
    if direction.lower() == "w" and [x,y-1] not in wall :
      self.y -= 1
    elif direction.lower() == "s" and [x,y+1] not in wall :
      self.y += 1
    elif direction.lower() == "a" and [x-1,y] not in wall :
      self.x -= 1
    elif direction.lower() == "d" and [x+1,y] not in wall :
      self.x += 1
  def info(self,name,description):
    return {"name":name,"description":description}



