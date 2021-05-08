from tkinter import *
from tkinter import ttk
import PIL
from PIL import ImageTk
from PIL import Image

def getcoordinate(event):
    print(str(event.x)+","+str(event.y))

frame = Tk()
frame.title("Coordinatator Accesor")

image = ImageTk.PhotoImage(Image.open("cert_alumni.jpg"))


fcanvas = Canvas(frame,width="4960", height="7016",background="white");
can_img = fcanvas.create_image(0,0,image=image, anchor=NW)
fcanvas.pack()

scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=fcanvas.yview)
scroll.pack(side=RIGHT, fill=Y)

fcanvas.configure(yscrollcommand=scroll.set)#set the scrollbar command
fcanvas.bind('<Configure>', lambda e: fcanvas.configure(scrollregion = fcanvas.bbox('all')))

fcanvas.bind('<Button-1>',getcoordinate)



frame.mainloop()