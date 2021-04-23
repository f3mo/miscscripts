import json
import sys
import requests
from urllib.parse import urlparse
import re
from time import  sleep
filename= []
file_handle = []
ext = []
file_name = []
file_size = []
directory = sys.argv[2]

url = ''
def parse_url():
    if '4chan' in sys.argv[1]:
        global controller
        controller = 'https://a.4cdn.org'
        global netlock
        netlock = urlparse(sys.argv[1]).path
        netlock = re.findall(r'\/\w+\/', netlock)
        url = controller + urlparse(sys.argv[1]).path + '.json'
        return(url)
    else:
        controller = 'https://wizchan.org/'
        netlock = urlparse(sys.argv[1]).path
        netlock = re.findall(r'\/\w+\/', netlock)
        url = sys.argv[1].replace('.html', '.json')
        return(url)



def  get_data(url):
    r = requests.get(url)
    return(r.content)

def main():
    data = json.loads(get_data(parse_url()))
    if 'posts' in data:
        for keys in data['posts']:
            if 'tim'  and 'ext' and  'filename' and 'fsize' in keys:
                filename.append(str(keys['tim'])  + keys['ext'])
                file_handle.append(str(keys['filename'])   + keys['ext'] ) 
                file_size.append(str(keys['fsize'] / 100 ))
    else:
        sys.exit()

    # DOWNLOAD FILES 
    counter =  0
    print(f'Total of {len(filename)} files')
    for i, x, y in zip(filename, file_handle, file_size):
        url2  = controller + netlock[0] + i
        if '4cdn' in controller:
            url2 = url2.replace('a', 'i')
        else:
            url2= f'{controller}{netlock[0]}src/{i}'
        counter += 1
        print(f' Donloading {x} {y} -KB  {counter}/{len(filename)}' )
        data = get_data(url2)
        sleep(4)
        with open(directory+ x, 'wb') as f:
            f.write(data)

if __name__ == '__main__':
    main()