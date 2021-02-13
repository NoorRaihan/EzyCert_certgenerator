from PIL import Image, ImageFont, ImageDraw
import pandas
import pdf2image
import os.path
from os import path
import time 

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
  --FOR PERSONAL & COMPASS USE ONLY-- 
  [Always Generate Signature First]
 # RENAME ur excel to filename.xlsx #
          
    '''

choice = '''
[1] Generate E-Certificate
[2] Double Checking E-Certificate
[3] Generate single E-Certificate
[4] Adding Signature to Certificate (in development)
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


def generate_cert(): #for generating multiple certificate
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
      font = ImageFont.truetype("arial.ttf",90)
      w,h = font.getsize(i)
      draw.text(((3500-w)/2,(2500-h)/2), i, (0,0,0), font=font)
      print("\033[1;32;40mGenerating certificate for",i,"\033[1;37;40m")
      cert.save(filepath + "/cert_" + i + ".pdf")


def check_cert(): #for checking all the cert based on excel namelist
  dir_check = False

  while dir_check == False:
    filepath = input("Cert folder: ")
    dir_check = path.exists(filepath)
    if dir_check == False:
      print("\033[1;31;40mDirectory does not exist \033[1;37;40m")

  for i in name_list:
    cert_name = filepath + "/cert_" + i +".pdf"
    ext = path.exists(cert_name)
    if ext == True:
        print("\033[1;32;40mCertificate for",i,"is exist\033[1;37;40m")
    else:
        print("\033[1;31;40mCertificate for",i,"is missing \033[1;37;40m")

def singleGenerate(): #for generate single certificate
  dir_check = False
  name = input("\nFullname: ")
  while dir_check == False:
      cert_path = input("Enter your template path: ")
      dir_check = path.exists(cert_path)
      if dir_check == False:
        print("\033[1;31;40mFile does not exist \033[1;37;40m")
  
  cert = Image.open(cert_path)
  draw = ImageDraw.Draw(cert)
  font = ImageFont.truetype("arial.ttf",90)
  w,h = font.getsize(name)
  draw.text(((3500-w)/2,(2500-h)/2), name, (0,0,0), font=font)
  print("\033[1;32;40mGenerating certificate for",name,"\033[1;37;40m")
  cert.save("cert_" + name + ".pdf")

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

 
u_choice = int(input("Choice: "))
if u_choice == 1:
  generate_cert()
if u_choice == 2:
  check_cert()
if u_choice == 3:
  singleGenerate()
if u_choice == 4:
  addSignature()

