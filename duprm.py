from hashlib import md5
from os import path, listdir, remove
from base64 import b64encode
from sys import argv, exit

def get_file_list():
	file_list = []
	if len(argv) < 2 or path.isdir(argv[1]) != True:
		print('Choose a directory')
		exit(5)	
	else:
		for file_ in listdir(argv[1]):
			if path.isfile(path.join(argv[1], file_)) == True:	
				file_list.append(path.join(argv[1], file_))
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
	for key, value  in zip(file_hash_map, file_hash_map.values()):
		if key not in sorted_files and value not in sorted_files.values():
			sorted_files[key] = value
		if key not in sorted_files:
			duplicates.append(key)
	print(f' {len(duplicates)} duplicates Found')
	for key in file_hash_map: 
		if key not in  sorted_files:
			remove(key)
			print(f' File {key} was deleted')

if __name__ == '__main__':
    main()
