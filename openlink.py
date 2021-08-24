import os
import sys

for file in sys.argv[1:]:
    if os.path.exists(file):
        with open(file) as f:
            link = f.read()
        os.system(f'open {link}')

