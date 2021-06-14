import os
import sys
import argparse

def get_dir(dir_):
    file_path = []
    for root, dirs, files in os.walk(dir_):
        for file_ in files:
            file_path.append(root+file_)
    return file_path

def main():
    parser = argparse.ArgumentParser(usage=f'{sys.argv[0]} [dir] [name]')
    parser.add_argument('directory', type=str)
    parser.add_argument('pattern', type=str)
    args = parser.parse_args()
    if os.path.isdir(args.directory) and args.pattern:
         files = get_dir(args.directory)
         for file_, rg in zip(files, range(1, len(files))):
             os.replace(file_, file_.replace(file_.split('/')[-1], f'{args.pattern}{rg}.{file_.split(".")[-1]}'))
         print(f' All {len(files)} files renamed\n')
    else:
        print(parser.format_usage())

if __name__ == '__main__':
    main()
