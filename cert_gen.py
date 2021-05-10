from PIL import Image, ImageFont, ImageDraw
import pandas
import os.path
import os
from os import path
import time 
import json

banner = ''' 
  ______            _____          _   
 |  ____|          / ____|        | |  
 | |__   _____   _| |     ___ _ __| |_ 
 |  __| |_  / | | | |    / _ \ '__| __|
 | |____ / /| |_| | |___|  __/ |  | |_ 
 |______/___|\__, |\_____\___|_|   \__|
              __/ |                    
             |___/                     
        AUTHOR : NOOR RAIHAN
          
    '''

choice = '''
[1] Generate E-Certificate
[2] Double Checking E-Certificate
[3] Generate single E-Certificate
[4] Adding Signature to Certificate (in development)
[5] Generate E-certification (with IC)
[6] Generate single E-certification (with IC)
[7] Set new coordinate
'''

print(banner)
print(choice)

dir_check2 = False
while dir_check2 == False:
  ex_file = input("Enter excel filepath (.xlsx): ")
  dir_check2 = path.exists(ex_file)
  if dir_check2 == False:
    print("\033[1;31;40mFile does not exist \033[1;37;40m")

    
name = pandas.read_excel(ex_file)
name_list = name['Name'].tolist()

#read JSON file to get coordinate
def readJSON():
  with open('coordinate.json') as jsonfile:
    data = json.load(jsonfile)
    for dat in data['coordinate']:
      x = dat['x-axis']
      y = dat['y-axis']
      fontsize = dat['fontsize']
  
  return x, y, fontsize

def generateWithIC(x,y,fontsize):
  dir_check = False
  ic_list = name['IC'].tolist()

  while dir_check == False:
      cert_path = input("Enter your template path: ")
      dir_check = path.exists(cert_path)
      if dir_check == False:
        print("\033[1;31;40mFile does not exist \033[1;37;40m")
  
  
  filepath = input("Save to (folder): ")
  o_folder = os.system("mkdir " + filepath)
  print("\033[1;33;40mTotal name : " + str(len(name_list)) + "\033[1;37;40m")
  time.sleep(5)

  for i, z in zip(name_list, ic_list):
    z = str(z)
    cert = Image.open(cert_path)
    draw = ImageDraw.Draw(cert)
    font = ImageFont.truetype("arial.ttf",fontsize)
    w,h = font.getsize(i)
    w2,h2 = font.getsize(z)
    draw.text((x,y), i, (0,0,0), anchor="mm",font=font)
    draw.text((x,(y+(y*0.1))), "("+z+")", (0,0,0), anchor="mm",font=font)
    print("\033[1;32;40mGenerating certificate for",i,"\033[1;37;40m")
    cert.save(filepath + "/cert_" + i + ".pdf")
  os.system('pause')

def singleGenerateWithIC(x,y,fontsize): #for generate single certificate
  dir_check = False
  name = input("\nFullname: ")
  ic = input("\IC Number: ")
  while dir_check == False:
      cert_path = input("Enter your template path: ")
      dir_check = path.exists(cert_path)
      if dir_check == False:
        print("\033[1;31;40mFile does not exist \033[1;37;40m")
  
  cert = Image.open(cert_path)
  draw = ImageDraw.Draw(cert)
  font = ImageFont.truetype("arial.ttf",fontsize)
  w,h = font.getsize(name)
  w2, h2 = font.getsize(ic)
  draw.text((x,y), name, (0,0,0), anchor="mm",font=font)
  draw.text((x,y+(y*0.1)), "("+str(ic)+")", (0,0,0), anchor="mm",font=font)
  print("\033[1;32;40mGenerating certificate for",name,"\033[1;37;40m")
  cert.save("cert_" + name + ".pdf")
  os.system('pause')


def generate_cert(x,y,fontsize): #for generating multiple certificate
  dir_check = False

  while dir_check == False:
      cert_path = input("Enter your template path: ")
      dir_check = path.exists(cert_path)
      if dir_check == False:
        print("\033[1;31;40mFile does not exist \033[1;37;40m")
  
  filepath = input("Save to (folder): ")
  o_folder = os.system("mkdir " + filepath)
  print("\033[1;33;40mTotal name : " + str(len(name_list)) + "\033[1;37;40m")
  time.sleep(5)
  
  for i in name_list:
      cert = Image.open(cert_path)
      draw = ImageDraw.Draw(cert)
      font = ImageFont.truetype("arial.ttf",fontsize)
      w,h = font.getsize(i)
      draw.text((x,y), i.upper(), (0,0,0), anchor="mm",font=font)
      print("\033[1;32;40mGenerating certificate for",i,"\033[1;37;40m")
      cert.save(filepath + "/cert_" + i + ".pdf")
  os.system('pause')


def check_cert(): #for checking all the cert based on excel namelist
  dir_check = False

  while dir_check == False:
    filepath = input("Cert folder: ")
    dir_check = path.exists(filepath)
    if dir_check == False:
      print("\033[1;31;40mDirectory does not exist \033[1;37;40m")

  miss = 0
  for i in name_list:
    cert_name = filepath + "/cert_" + i +".pdf"
    ext = path.exists(cert_name)
    if ext == True:
        print("\033[1;32;40mCertificate for",i,"is exist\033[1;37;40m")
    else:
        print("\033[1;31;40mCertificate for",i,"is missing \033[1;37;40m")
        miss +=1
  print("\n",miss, "file missing")
  os.system('pause')

def singleGenerate(x,y,fontsize): #for generate single certificate
  dir_check = False
  name = input("\nFullname: ")
  while dir_check == False:
      cert_path = input("Enter your template path: ")
      dir_check = path.exists(cert_path)
      if dir_check == False:
        print("\033[1;31;40mFile does not exist","\033[1;37;40m")
  
  cert = Image.open(cert_path) 
  draw = ImageDraw.Draw(cert)
  font = ImageFont.truetype("arial.ttf",fontsize)
  w,h = font.getsize(name)
  draw.text((x,y), name, (0,0,0), anchor="mm",font=font)
  print("\033[1;32;40mGenerating certificate for",name,"\033[1;37;40m")
  cert.save("cert_" + name + ".pdf")
  os.system('pause')

def addSignature(): #adding a signature
  dir_check = False
  while dir_check == False:
      cert_path = input("Enter your template path: ")
      dir_check = path.exists(cert_path)
      if dir_check == False:
        print("\033[1;31;40mFile does not exist \033[1;37;40m")

  foreground = Image.open("logotest.png")
  background = Image.open(cert_path)
  newf = foreground.resize((1200,1200), Image.ANTIALIAS)
  background.paste(newf,(1000,0), newf)
  print("\033[1;32;40mAdding Signature to Certificate\033[1;37;40m")
  background.save("new_signature_template.jpg")


x,y,fontsize = readJSON()

u_choice = int(input("Choice: "))
if u_choice == 1:
  generate_cert(x,y,fontsize)
elif u_choice == 2:
  check_cert()
elif u_choice == 3:
  singleGenerate(x,y,fontsize)
elif u_choice == 4:
  addSignature()
elif u_choice == 5:
  generateWithIC(x,y,fontsize)
elif u_choice == 6:
  singleGenerateWithIC(x,y,fontsize)
elif u_choice == 7:
  os.system('.\coordinate.exe')

