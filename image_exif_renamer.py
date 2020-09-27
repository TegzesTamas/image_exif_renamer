#! /usr/bin/env python3

from os import rename
from os.path import split, join, splitext
from argparse import ArgumentParser
from exif import Image
from datetime import datetime
from traceback import print_exc


def rename_file_based_on_exif(path):
    with open(path, 'rb') as image_file:
        image = Image(image_file)
    dt = datetime.strptime(image.datetime_original, '%Y:%m:%d %H:%M:%S')
    filename = dt.strftime('%Y%m%d-%H%M%S')
    head, tail = split(path)
    _, ext = splitext(tail)
    new_path = join(head, filename + ext)
    rename(path, new_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("file",
                        nargs='+')
    args = parser.parse_args()
    for file in args.file:
        try:
            rename_file_based_on_exif(file)
        except Exception as e:
            print(f'An exception occured while processing "{file}"')
            print_exc()
