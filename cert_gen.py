from asyncio.windows_events import NULL
from PIL import Image, ImageFont, ImageDraw
from numpy import true_divide
import pandas
import os.path
import os
import coordinate
from os import path
import time 
import json
import sys

banner = ''' 
  ______            _____          _   
 |  ____|          / ____|        | |  
 | |__   _____   _| |     ___ _ __| |_ 
 |  __| |_  / | | | |    / _ \ '__| __|
 | |____ / /| |_| | |___|  __/ |  | |_ 
 |______/___|\__, |\_____\___|_|   \__|
              __/ |                    
             |___/          
              
              V2.0           
        AUTHOR : NOOR RAIHAN
          
    '''

choice = '''
[1] Generate Multiple E-Certificate
[2] Generate Single E-Certificate
[3] Configurations
[4] Exit
'''
choiceMultiple = '''
[1] Generate E-Certificate
[2] Generate E-certification (with IC)
[3] Back
'''

choiceSingle = '''
[1] Generate single E-Certificate
[2] Generate single E-certification (with IC)
[3] Back
'''

choiceConfig ='''
[1] Reposition
[2] Choose font
[3] Back
'''

#list of globals variables
excel_file = NULL
name = NULL
name_list = []
x = 0
y = 0
fontsize = 0
fontname = NULL
cert_path = NULL

def menu_Multiple():
  os.system('cls')
  print(banner)
  print(choiceMultiple)
  inp = int(input('Choose: '))

  flag = True

  while (flag):
    if inp == 1:
      generate_cert()
      break
    elif inp == 2: 
      generateWithIC()
      break
    elif inp == 3:
      menu()
      break
    elif inp == 4:
      sys.exit(0)
    else:
      print('Invalid input')

def menu_Single():
  os.system('cls')
  print(banner)
  print(choiceSingle)
  inp = int(input('Choose: '))

  flag = True

  while (flag):
    if inp == 1:
      singleGenerate()
      break
    elif inp == 2: 
      singleGenerateWithIC()
      break
    elif inp == 3:
      menu()
      break
    else:
      print('Invalid input')

def menu_Config():
  os.system('cls')
  print(banner)
  print(choiceConfig)
  inp = int(input('Choose: '))

  flag = True

  while (flag):
    if inp == 1:
      coordinate.main()
      os.system('pause')
      menu()
      break
    elif inp == 2: 
      config_Font()
      break
    elif inp == 3:
      menu()
      break
    else:
      print('Invalid input')

def config_Font():
  counter = 0
  path = 'bin/fonts/'
  listFont = os.listdir(path)
  for font in listFont:
    print("["+str(counter + 1)+"]", font)
    counter += 1
  
  inp = int(input('Choose font: '))
  f_index = inp - 1

  with open('coordinate.json') as jsonfile:
      datas = json.load(jsonfile)
  for data in datas['coordinate']:
      data['font'] = path + listFont[f_index]

  with open('coordinate.json','w') as output:
      json.dump(datas, output)
  print("Successfully save the font!")
  os.system('pause')
  menu()


#get the excel and file
def get_File():
  global excel_file, name, name_list

  dir_check2 = False
  while dir_check2 == False:
    ex_file = input("Enter excel filepath (.xlsx): ")
    dir_check2 = path.exists(ex_file)
    if dir_check2 == False:
      print("\033[1;31;40mFile does not exist \033[1;37;40m")
  
  try:
    name = pandas.read_excel(ex_file)
    name_list = name['Name'].tolist()
  except Exception:
    print("Can't find Name in file")

#read JSON file to get coordinate
def readJSON():
  global x, y, fontsize, fontname

  with open('coordinate.json') as jsonfile:
    datas = json.load(jsonfile)
    for data in datas['coordinate']:
      x = int(data['x-axis'])
      y = int(data['y-axis'])
      fontsize = int(data['fontsize'])
      fontname = data['font']
  
  return x, y, fontsize, fontname

def get_Template():
  global cert_path
  dir_check = False

  while dir_check == False:
      cert_path = input("Enter your template path [must be in .jpg or .png]: ")
      dir_check = path.exists(cert_path)
      if dir_check == False:
        print("\033[1;31;40mFile does not exist \033[1;37;40m")

#generate certificate with IC
def generateWithIC():
  global name, name_list
  get_File()
  get_Template()
  readJSON()

  filepath = input("Save to (folder): ")
  try:
    ic_list = name['IC'].tolist()
  except Exception:
    print("IC can not be found in the file")

  print("\033[1;33;40mTotal name : " + str(len(name_list)) + "\033[1;37;40m")
  time.sleep(5)
  
  filepath = "outputs/" + filepath
  
  try:
    os.makedirs(filepath, exist_ok = True)
  except OSError as err:
    print('Directory', filepath, "can not be created")

  for i, z in zip(name_list, ic_list):
    cert_generateIC(i,z,filepath)
  os.system('pause')
  menu()


#for generate single certificate
def singleGenerateWithIC():
  get_Template()
  readJSON()

  name = input("\nFullname: ")
  ic = input("IC Number: ")
  filepath = "outputs"
  cert_generateIC(name, ic, filepath)
  os.system('pause')
  menu()

#for generating multiple certificate
def generate_cert():
  get_File()
  get_Template()
  readJSON()

  filepath = input("Save to (folder): ")
  print("\033[1;33;40mTotal name : " + str(len(name_list)) + "\033[1;37;40m")
  time.sleep(5)
  
  filepath = "outputs/" + filepath
  
  try:
    os.makedirs(filepath, exist_ok = True)
  except OSError as err:
    print('Directory', filepath, "can not be created")

  for i in name_list:
    cert_generate(i, filepath)

  os.system('pause')
  menu()

#for checking all the cert based on excel namelist
def check_cert():
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
  menu()

#for generate single certificate
def singleGenerate():
  get_Template()
  readJSON()

  name = input("\nFullname: ")
  filepath = "outputs"
  cert_generate(name,filepath)
  os.system('pause')
  menu()

#algortihm to generate the certificate
def cert_generate(name, filepath):
  global x,y,fontname,fontsize,cert_path

  name = name.upper()
  new_name = name_sanitize(name)
  new_name = new_name.upper()

  try:
    cert = Image.open(cert_path)
    draw = ImageDraw.Draw(cert)
    font = ImageFont.truetype(fontname,fontsize)
    w,h = font.getsize(name)
    draw.text((x,y), name.upper(), (0,0,0), anchor="mm",font=font)
    print("\033[1;32;40mGenerating certificate for",name,"\033[1;37;40m")
    cert.save(filepath + "/cert_" + new_name + ".pdf")
  except Exception as err:
    print("Failed generate: ", err)


#algortihm to generate the certificate with IC
def cert_generateIC(name, ic, filepath):
  global x,y,fontname,fontsize,cert_path

  name = name.upper()
  new_name = name_sanitize(name)
  new_name = new_name.upper()
  ic = ic_sanitize(ic)

  try:
      cert = Image.open(cert_path)
      draw = ImageDraw.Draw(cert)
      font = ImageFont.truetype(fontname,fontsize)
      w,h = font.getsize(name)
      w2,h2 = font.getsize(ic)
      draw.text((x,y), name, (0,0,0), anchor="mm",font=font)
      draw.text((x,(y+(y*0.1))), ic, (0,0,0), anchor="mm",font=font)
      print("\033[1;32;40mGenerating certificate for",name,"\033[1;37;40m")
      cert.save(filepath + "/cert_" + new_name + ".pdf")
  except Exception as err:
      print("Failed generate: ", err)
  
def name_sanitize(name):
  #sanitizing the indian name that lead to bug
  name = name.upper()
  if "A/L" in name: 
    name = name.replace("A/L", "")
  elif "A/P" in name:
    name = name.replace("A/P", "")
  
  return name

def ic_sanitize(ic):
  #sanitizing the ic by adding - 
  if "-" not in ic:
    new_ic = ic[0:6] + "-" + ic[6:8] + "-" + ic[8:12]
  else:
    new_ic = ic
  
  return new_ic

#adding a signature
# def addSignature():
#   dir_check = False
#   while dir_check == False:
#       cert_path = input("Enter your template path: ")
#       dir_check = path.exists(cert_path)
#       if dir_check == False:
#         print("\033[1;31;40mFile does not exist \033[1;37;40m")

#   foreground = Image.open("logotest.png")
#   background = Image.open(cert_path)
#   newf = foreground.resize((1200,1200), Image.ANTIALIAS)
#   background.paste(newf,(1000,0), newf)
#   print("\033[1;32;40mAdding Signature to Certificate\033[1;37;40m")
#   background.save("new_signature_template.jpg")

def menu():
  os.system('cls')
  print(banner)
  print(choice)
  u_choice = int(input("Choice: "))
  if u_choice == 1:
    menu_Multiple()
  elif u_choice == 2:
    menu_Single()
  elif u_choice == 3:
    menu_Config()

if __name__ == "__main__":
  menu()

