import pandas
import os.path
from os import path


name = pandas.read_excel(r"esportname.xlsx")

name_list = name['Name'].tolist()


for i in name_list:

    cert_name = "cert_" + i +".pdf"
    ext = path.exists(cert_name)
    if ext == True:
        print("Certificate for",i,"is exist")
    else:
        print("\033[1;31;40m Certificate for",i,"is missing")



