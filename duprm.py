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

def main():
	file_hash_map = hash_file_list()
	sorted_files = {}
	duplicates = []
	user = getpass.getuser()
	linux_trash = f'/home/{user}/.local/share/Trash/files/'
	for key, value  in zip(file_hash_map, file_hash_map.values()):
		if key not in sorted_files and value not in sorted_files.values():
			sorted_files[key] = value
		if key not in sorted_files:
			duplicates.append(key)
	print(f"Total of {len(duplicates)}")
	for files in duplicates:
		print(files)
	user_input = input('\n Do you want to continue? [y/n]: \n')


	if user_input == 'n':
		exit(3)
	elif user_input == 'y':
		for key in file_hash_map: 
			if key not in  sorted_files:
				if platform.startswith('linux'):
					replace(key,linux_trash+key.split('/')[-1] )
				elif platform.startswith('windows'):
					remove(key)
				print(f' File {key.split("/")[-1]} was deleted')
	else:
		exit(5)

if __name__ == '__main__':
    main()
