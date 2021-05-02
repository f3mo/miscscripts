import json
from sys import argv, exit
import requests
from urllib.parse import urlparse
import re
from time import  sleep
import os

def request_data(url):
  r = requests.get(url)
  if r.status_code == 200:
    return r.content
  else:
    print('404:PAGE NOT FOUND')


def parse_argv():
  if len(argv) < 3 or 'chan' not in argv[1]:
    print (len(argv))
    exit(2)
  elif '4chan' in argv[1]:
    netloc_4chan = 'a.4cdn.org'
    netloc_ = urlparse(argv[1]).netloc
    url = argv[1].replace(netloc_, netloc_4chan)
    return url + '.json'
  elif 'wizchan' in argv[1]:
    return argv[1].replace('.html', '.json')

def parse_json():
  json_data = request_data( parse_argv())
  json_data = json.loads(json_data)
  file_data = {}
  for key in json_data['posts']:
    if 'filename' and 'tim' and 'ext' in key.keys():
      if '4chan' in argv[1]:
        url = 'https://i.4cdn.org/'
        path_4 = urlparse(argv[1]).path
        path_4 = path_4.split('/')[1]
        file_data[key['filename'] + key['ext']] = url + path_4 + '/' + str(key['tim'])   + key['ext']
      else:
        url = 'https://wizchan.org/'
        path_4 = urlparse(argv[1]).path
        path_4 = path_4.split('/')[1] + '/src/'
        file_data[key['filename'] + key['ext']] = url + path_4 +  str(key['tim'])   + key['ext']
  return file_data

def check_files():
  file_data = parse_json()
  for files_ in os.listdir(argv[2]):
    if files_ in file_data.keys():
      file_data.pop(files_) 
  return file_data
  
def main():
  file_data = check_files()
  if file_data == 0:
    print('Files already in directory')
  else:
    counter = 0
    print(f' Total of {len(file_data.keys())} will be downloaded')
    for file_ in file_data:
    counter = counter +1
    with open(os.path.join(argv[2], file_), 'wb') as f:
    f.write(request_data( file_data[file_]))
    print(f' Downloading {file_}  {counter} / {len(file_data.keys())}')
    
  
if __name__ == '__main__':
  main()
