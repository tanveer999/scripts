import os
import argparse

def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=True)

    return parser.parse_args()

def rename_files_in_a_directory(directory):

    for filename in os.listdir(directory):
        new_filename = filename.replace(' ', '-').lower()

        absolute_filename = os.path.join(directory, filename)
        absolute_new_filename = os.path.join(directory, new_filename)
        print(f'Renaming {absolute_filename} to {absolute_new_filename}')
        if new_filename != filename:
            os.rename(absolute_filename, absolute_new_filename)

def rename_all_files(directory):
    """
        Rename all files in a directory and sub-directory and also rename the sub-directory
    """

    for path, folders, files in os.walk(directory):
        for filename in files:
            os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ', '-').lower()))

        for i in range(len(folders)):
            new_folder_name = folders[i].replace(' ', '-').lower()
            os.rename(os.path.join(path, folders[i]), os.path.join(path, new_folder_name))
            folders[i] = new_folder_name

if __name__ == '__main__':
    args = read_args()
    # rename_files_in_a_directory(args.directory)
    rename_all_files(args.directory)