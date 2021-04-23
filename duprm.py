import hashlib
import os
from sys import argv

def file_tb():
    file_dict = {}
    files = os.listdir(argv[1])
    if len(argv) < 2:
        exit()
    else:
        for file in files:
            with open(argv[1]+file, 'rb')as f:
                file_dict[argv[1] +file] = hashlib.md5(f.read()).hexdigest()
        return file_dict

file_dict = file_tb()
n_dict = {}
for i , o in zip(file_dict.keys(), file_dict.values()):
    if i  not in n_dict.keys() and o not in n_dict.values():
        n_dict[i] = o
for i in file_dict.keys():
    if i not in n_dict.keys():
        print(f'File { i.split("/")[-1] } has been deleted')
        os.remove(i)