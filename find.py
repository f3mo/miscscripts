#!/usr/bin/env python3
import os 
import sys

def main():
  txt_file  = '/tmp/find.txt'
  files = []

  if len(sys.argv) < 2:
    print('Enter search term')
  else:
    if os.path.isfile(txt_file):
      with open(txt_file, 'rt') as f:
        files.append(f.readlines())
        for i in files: 
          for o in i: 
            if sys.argv[1] in o:
              print(o)
    else:
      with open(txt_file, 'wt')as f:
        for root , dirs, file_ in os.walk('/'):
          for files_ in file_:
             f.writelines(f'{root}+{files_}\n')
             files.append(root+files_)
      for i in files:
        if sys.argv[1] in i: 
          print(i)

if __name__ == "__main__":
    main()
