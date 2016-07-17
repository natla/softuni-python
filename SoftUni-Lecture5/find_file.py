# Задача: 1. Търсене във файловата система

import os
import sys

if len(sys.argv) < 3:
    print("You need to provide directory and filename in the terminal: python find-file.py <dir> <filename>")
elif not os.path.exists(sys.argv[1]):
    print("Directory doesn't exist")
else:
    search_dir = sys.argv[1]
    search_file = sys.argv[2]
    found = []
    for root, dirs, files in os.walk(search_dir):
        if os.path.isfile(os.path.join(root, search_file)):
            result = os.path.dirname(os.path.join(root, search_file))
            found.append(result)  # if the file is found more than once the results get appended to a list
    if len(found) == 0:
        print("File not found")
    else:
        print('\n'.join(found))
