# Samuel Kim - 027845491

import sys

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

file_name = sys.argv[1]
content = read_file(file_name)
print(content)

