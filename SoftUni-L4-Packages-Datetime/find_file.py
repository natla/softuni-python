"""
Задача: 1. Търсене във файловата система
Допълнение на задачата:
Разширете вашия код, така че да може да търсите с прост wild card * - в началото или в края на името.
"""

import os
import sys
from fnmatch import fnmatch

if len(sys.argv) < 3:
    print("You need to provide directory and at least part of the filename in the terminal:\n"
          "python find_file.py <dir> <filename> or python find_file.py <dir> <*file_part*>")
elif not os.path.exists(sys.argv[1]):
    print("Directory doesn't exist")
else:
    search_dir = sys.argv[1]
    search_file = sys.argv[2]

    found = []
    for root, dirs, files in os.walk(search_dir):
        path = os.path.join(root, search_file)
        if os.path.isfile(path):
            result = os.path.dirname(path)
            found.append(result)
        else:
            for file in files:
                if fnmatch(file, search_file):
                    result = root
                    if result not in found:
                        found.append(result)

    if len(found) > 0:
        print("These directories contain file(s) {}:\n{}".format(search_file, '\n'.join(found)))
    else:
        print("File not found")
