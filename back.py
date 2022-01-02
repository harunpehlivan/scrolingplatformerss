from tkinter import *
class Back:
  def __init__(self, window, colour="blue",width=600, height=400):
        self.window = window
        self.width = width
        self.height = height
        self.colour = colour
        self.canvas = Canvas(self.window, bg=self.colour, height=self.height, width=self.width)
        self.canvas.pack()
  def draw_rectangle(self, rectangle, inte):
        x1 = rectangle.__dict__["x_position" + str(inte)]
        x2 = rectangle.__dict__["x_position" + str(inte)] + rectangle.__dict__["width" + str(inte)]
        y1 = rectangle.__dict__["y_position" + str(inte)]
        y2 = rectangle.__dict__["y_position" + str(inte)] + rectangle.__dict__["height" + str(inte)]
        c = rectangle.__dict__["Colour" + str(inte)]
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)
  def draw_rectangle2(self, rectangle, inty, i):
       x1 = rectangle.__dict__["x_position" + str(inty+1)]
       x2 = rectangle.__dict__["x_position" + str(inty+1)] +  rectangle.width
       y1 = rectangle.__dict__["y_position" + str(i+1)]
       y2 = rectangle.__dict__["y_position" + str(i+1)] + rectangle.height
       c = rectangle.colour
       return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)
  def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)
  def remove_item(self, item):
    self.canvas.delete(item)
  def change_item_colour(self, item, c):
    self.canvas.itemconfigure(item, fill=c)
  def end_load(self):
    self.width = self.width/2
    self.canvas = Canvas(self.window, bg=self.colour, height=self.height, width=self.width)
    self.canvas.pack()