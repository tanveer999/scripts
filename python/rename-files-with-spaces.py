import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', required=True)
args = parser.parse_args()

directory = args.directory.strip()

for filename in os.listdir(directory):
    new_filename = filename.replace(' ', '-').lower()
    print(f'Renaming {filename} to {new_filename}')
    if new_filename != filename:
        os.rename(f'{directory}{filename}', f'{directory}{new_filename}')