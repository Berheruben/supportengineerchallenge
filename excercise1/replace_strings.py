import os
import sys

def replace_strings_in_file(file_path, old_string, new_string):
    with open(file_path, 'r') as file:
        file_data = file.read()

    file_data = file_data.replace(old_string, new_string)

    with open(file_path, 'w') as file:
        file.write(file_data)

def replace_strings_in_directory(directory_path, old_string, new_string):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                replace_strings_in_file(file_path, old_string, new_string)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python replace_strings.py <old_string> <new_string> <directory_path>")
        sys.exit(1)

    old_string = sys.argv[1]
    new_string = sys.argv[2]
    directory_path = sys.argv[3]

    replace_strings_in_directory(directory_path, old_string, new_string)
        
