from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image
from PIL import ImageTk
from PIL import ImageDraw, ImageFont
import os.path
from os import path
import json

dir_check = False
while dir_check == False:
      image_path = input("Enter your template path: ")
      dir_check = path.exists(image_path)
      if dir_check == False:
        print("\033[1;31;40mFile does not exist \033[1;37;40m")


root = Tk()
img = Image.open(image_path)
img = img.resize((877,620), Image.ANTIALIAS)
image = ImageTk.PhotoImage(img)



def writeJson(x,y):
    data = {}
    data['coordinate'] = []
    data['coordinate'].append({
        'x-axis' : x,
        'y-axis' : y 
    })
    with open('coordinate.json','w') as output:
        json.dump(data, output)
    print("Successfully save the coordinate!")
    root.destroy()


def getCoordinate(event):
    x = event.x * 4
    y = event.y * 4
    print(str(x)+","+str(y))
    singleGenerate(x, y)
    
def singleGenerate(x,y): #for generate single certificate
  dir_check = False
  test = "THIS IS A TEST NAME FOO GG BOII"
  cert = Image.open(image_path)
  draw = ImageDraw.Draw(cert)
  font = ImageFont.truetype("arial.ttf",90)
  w,h = font.getsize(test)
  draw.text((x,y), test, (0,0,0),anchor="mm",font=font)
  cert.show()
  ask = input("confirm? [y/n]: ")
  if ask == "y":
    writeJson(x, y)
  else:
      pass

canv = Canvas(root,width="1240", height="1754")
canv.pack()
canv.create_image(0,0,image=image, anchor=NW)
canv.bind('<Button-1>',getCoordinate)

root.mainloop()



