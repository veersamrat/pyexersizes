import os

def read_txt_file(path):
    with open(path,'r') as txtf:
        print(txtf.read().replace("\n"," "))
        
path = "./Sample1.txt"
read_txt_file(path)
