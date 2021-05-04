from hashlib import md5
from os import path, listdir, replace, walk, remove
from base64 import b64encode
from sys import argv, exit, platform
import getpass

def get_file_list():
  file_list = []
  if len(argv) < 2 or path.isdir(argv[1]) != True:
    print('Choose a directory')
    exit(5) 
  else:
    for root, dirs, files in walk(argv[1]):
      for file_ in files:
        if path.isfile(path.join(root, file_)):
          file_list.append(path.join(root,file_))

  return file_list


def hash_file_list():
  file_list = get_file_list()
  file_hash_map = {}
  file_hash = ''
  for file_ in file_list:
    with open(file_, 'rb') as f:
      file_hash = md5(f.read()).digest()
      file_hash = b64encode(file_hash).decode()
      file_hash_map[file_] = file_hash
  return file_hash_map
def sort_files():
  file_dict = hash_file_list()
  dup_files = {}
  dup = {}
  og_file = {}
  og_file_list = []
  for key, value in file_dict.items():
    if key not in dup_files and value not in dup_files.values():
      dup_files[key] = value 
    if key not in dup_files:
      dup[key] = value
    if key not in dup.keys():
      og_file[key] = value
  for key, value in og_file.items():
      if value in dup.values():
          og_file_list.append(key)
  #print(og_file_list)
  return dup , og_file_list


def main():
  dup_files,  og_files = sort_files()
  user = getpass.getuser()
  linux_trash = f'/home/{user}/.local/share/Trash/files/'
  dup_files , og_files = sort_files()
  print(f' {len(og_files)} was found\n')
  for dup_f, og_f in zip(dup_files, og_files):
    print(f' Duplicate:  {dup_f}\n '
            f'original:  {og_f}\n')
  user_input = input(' Do you want to continue? [y/n]: ')
  if user_input == 'y':
    for key in dup_files.keys(): 
      if platform.startswith('linux'):
        replace(key,linux_trash+key.split('/')[-1] )
        print(f' \n File {key.split("/")[-1]} was deleted')
      elif platform.startswith('windows'):
        remove(key)
        print(f' File {key.split("/")[-1]} was deleted')
  else:
    exit(5)

if __name__ == '__main__':
    main()
