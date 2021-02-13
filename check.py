import pandas
import os.path
from os import path


name = pandas.read_excel(r"esportname.xlsx")

name_list = name['Name'].tolist()


for i in name_list:

    cert_name = "cert_" + i
    ext = path.exists(cert_name)
    if ext == True:
        print("Certificate for",i,"is exist")
    else:
        print(ext)


