from asyncio.windows_events import NULL
from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image
from PIL import ImageTk
from PIL import ImageDraw, ImageFont
import os.path
from os import path
import json

#list of variables
x = 0
y = 0
fontsize = 0
in_width = 0
in_height = 0
image_path = NULL
root = NULL



def writeJson():
    global root

    with open('coordinate.json') as jsonfile:
        datas = json.load(jsonfile)
    for data in datas['coordinate']:
        data['x-axis'] = str(data['x-axis']).replace(str(data['x-axis']), str(x))
        data['y-axis'] = str(data['y-axis']).replace(str(data['y-axis']), str(y))
        data['fontsize'] = str(data['fontsize']).replace(str(data['fontsize']), str(fontsize))
        data['font'] = data['font']

    with open('coordinate.json','w') as output:
        json.dump(datas, output)
    print("Successfully save the position!")
    root.destroy()


def getCoordinate(event):
    global x, y, in_height, in_width

    if(in_width > 1040 and in_height > 1040):
        x = event.x * 4
        y = event.y * 4
    else:
        x = event.x
        y = event.y
    print(str(x)+","+str(y))
    singleGenerate()
    
def singleGenerate():
    global fontsize, image_path

    test = "JOHN SMITH BIN AKHLAKEN"
    test2 = "000000-00-0000"
    cert = Image.open(image_path)
    draw = ImageDraw.Draw(cert)
    fontsize = 1
    font = ImageFont.truetype("arial.ttf",fontsize)

    while(font.getsize(test)[0] < cert.size[0]) and (font.getsize(test)[1] < cert.size[1]):
        fontsize +=1
        font = ImageFont.truetype("arial.ttf",fontsize)

    
    fontsize = int(fontsize/2)
    font = ImageFont.truetype("bin/fonts/arial.ttf",fontsize)
    draw.text((x,y), test, (0,0,0),anchor="mm",font=font)
    draw.text((x,(y+(y*0.1))), "("+str(test2)+")", (0,0,0), anchor="mm",font=font)
    cert.show()

def main():
    global in_width, in_height, image_path, root

    dir_check = False
    while dir_check == False:
        image_path = input("Enter your template path: ")
        dir_check = path.exists(image_path)
        if dir_check == False:
            print("\033[1;31;40mFile does not exist \033[1;37;40m")


    root = Tk()
    root.title('Positioning')
    img = Image.open(image_path)
    width, height = img.size
    in_width = width
    in_height = height
    print('Image Resolution:', width, height)
    if(width > 1040 and height > 1040):
        width = int(width/4)
        height = int(height/4)
        img = img.resize((width,height), Image.ANTIALIAS)

    image = ImageTk.PhotoImage(img)

    ttk.Button(root, text="Save Position", command=writeJson).pack()
    canv = Canvas(root,width=str(width), height=str(height))
    canv.pack()
    canv.create_image(0,0,image=image, anchor=NW)
    canv.bind('<Button-1>',getCoordinate)
    root.mainloop()

if __name__ == "__main__":
    main()



