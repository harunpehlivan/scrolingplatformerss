from tkinter import *
class Thing:
  def __init__(self, Back, width=6000, height=50, colour="white", x_position=10, y_position=350, x_speed=23, y_speed=23):
    self.width1 = width 
    self.height1 = height
    self.x_position1 = x_position
    self.y_position1 = y_position
    self.Colour1 = colour
    self.x_start = x_position
    self.y_start = y_position
    self.x_speed = x_speed
    self.y_speed = y_speed
    self.Back = Back
    self.rectangle = self.Back.draw_rectangle(self, 1)
  def moveL(self):
    #self.y_position1 -= self.y_speed
    self.x_position1 -= self.x_speed
    x1 = self.x_position1
    x2 = self.x_position1+self.width1
    y1 = self.y_position1
    y2 = self.y_position1+self.height1
    self.Back.move_item(self.rectangle, x1, y1, x2, y2)
  def moveR(self):
    #self.y_position1 -= self.y_speed
    self.x_position1 += self.x_speed
    x1 = self.x_position1
    x2 = self.x_position1+self.width1
    y1 = self.y_position1
    y2 = self.y_position1+self.height1
    self.Back.move_item(self.rectangle, x1, y1, x2, y2)
  def moveU(self):
    #self.y_position1 -= self.y_speed
    self.y_position1 -= self.y_speed
    x1 = self.x_position1
    x2 = self.x_position1+self.width1
    y1 = self.y_position1
    y2 = self.y_position1+self.height1
    self.Back.move_item(self.rectangle, x1, y1, x2, y2)
  def moveD(self):
    #self.y_position1 -= self.y_speed
    self.y_position1 += self.y_speed
    x1 = self.x_position1
    x2 = self.x_position1+self.width1
    y1 = self.y_position1
    y2 = self.y_position1+self.height1
    self.Back.move_item(self.rectangle, x1, y1, x2, y2)
  def selfc(self):
    self.Back.canvas.delete(self.rectangle)
  def shoot(self, master):
    self.y_position1 = master.y
    self.x_position1 = master.x
    x1 = self.x_position1
    x2 = self.x_position1+self.width1
    y1 = self.y_position1
    y2 = self.y_position1+self.height1
    self.Back.move_item(self.rectangle, x1, y1, x2, y2)
  def touching(self, selft):
    collision = False
    # Thing one
    top = self.y_position1
    bottom = self.y_position1 + self.height1
    left = self.x_position1
    right = self.x_position1 + self.width1 
    # Think big
    topt = selft.y_position1
    bottomt = selft.y_position1 + selft.height1
    leftt = selft.x_position1 
    rightt = selft.x_position1  + selft.width1
    if((bottomt > top) and (topt < bottom) and (rightt > left) and (leftt < right)):
      collision = True
    return collision