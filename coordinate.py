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
width, height = img.size
width = int(width/4)
height = int(height/4)
img = img.resize((width,height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(img)



def writeJson(x,y,fontsize):
    data = {}
    data['coordinate'] = []
    data['coordinate'].append({
        'x-axis' : x,
        'y-axis' : y, 
        'fontsize' : fontsize
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
    test2 = "00000000000"
    cert = Image.open(image_path)
    draw = ImageDraw.Draw(cert)
    fontsize = 1
    font = ImageFont.truetype("arial.ttf",fontsize)

    while(font.getsize(test)[0] < cert.size[0]) and (font.getsize(test)[1] < cert.size[1]):
        fontsize +=1
        font = ImageFont.truetype("arial.ttf",fontsize)

    
    fontsize = int(fontsize/2)
    font = ImageFont.truetype("arial.ttf",fontsize)
    draw.text((x,y), test, (0,0,0),anchor="mm",font=font)
    draw.text((x,(y+(y*0.1))), "("+str(test2)+")", (0,0,0), anchor="mm",font=font)
    cert.show()
    ask = input("confirm? [y/n]: ")
    if ask == "y":
        writeJson(x, y, fontsize)
    else:
        pass

canv = Canvas(root,width=str(width), height=str(height))
canv.pack()
canv.create_image(0,0,image=image, anchor=NW)
canv.bind('<Button-1>',getCoordinate)

root.mainloop()



