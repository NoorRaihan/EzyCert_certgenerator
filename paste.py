from PIL import Image, ImageFont, ImageDraw

foreground = Image.open("logotest.png")
background = Image.open("game_certtemp.jpg")
newf = foreground.resize((1200,1200), Image.ANTIALIAS)
background.paste(newf,(1000,0), newf)

background.save("pastetest.pdf")