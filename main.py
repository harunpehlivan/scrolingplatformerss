from tkinter import *
import back,square
window=Tk()
window.title("Sld")
backg = back.Back(window)
dimentions = {'X':[75,89,100,125,150,250,90,90], 'Y':[70,80,90,10,200,250,0,10]}
d=0
move1=0
move2=0
move3=0
floors = []
for i in range(len(dimentions['X'])):
  floors.append(square.Thing(backg, dimentions['X'][i], dimentions['Y'][i], "green", d, backg.height-dimentions['Y'][i], 10, 10))
  d+=dimentions['X'][i]
hitbox = square.Thing(backg, 50, 40, "Red", 15, 75, 25, 10)
player = square.Thing(backg, 50, 50, "Red", 15, 75, 25, 10)
def t():
  global move1, move2, move3
  tong2 = False
  ong2 = False
  for ob in floors:
    if tong2 := ob.touching(hitbox):
      ong2 = True
  if move1 == 1 and floors[0].x_position1 != 0 and not ong2:
    for ob in floors:
      ob.moveR()
    move1=0
  elif move2 == 2 and not ong2:
    for ob in floors:
      ob.moveL()
    move2=0
  ong = False
  tong = False
  for ob in floors:
    if tong := ob.touching(player):
      ong = True
  if not ong and move3 != 3:
    player.moveD()
    hitbox.moveD()
    if player.y_position1>=backg.height-player.height1:
      backg.window.withdraw()
      backg.window.quit()
  elif move3==3 and player.y_position1>=0:
    player.moveU()
    hitbox.moveU()
  if move3!=0:
    move3=0
  end = bool(floors[-1].touching(player))
  if not end:
    window.after(50, t)
def ml(master):
  global move1
  move1 = 1
def mr(master):
  global move2
  move2 = 2
def mu(master):
  global move3
  move3 = 3
window.bind("<Left>", ml)
window.bind("<Right>", mr)
window.bind("<Up>", mu)
t()