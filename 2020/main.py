import sys
from typing import Dict, List
from library import Library

# Books ids scanned by library
def read_input(filename):

    with open(filename, 'r') as f:

    #for index, line in enumerate(f):

        libraries = []

        data = f.readline()
        nbooks, nlibraries, days = list(map(int, data.split(" ")))

        scores = list(map(int, f.readline().split(" ")))

        for i in range(nlibraries):
            info = list(map(int, f.readline().split(" ")))

            books = list(map(int, f.readline().split(" ")))
            lib = Library(books, info[1], info[2], i)
            libraries.append(lib)

        return scores, libraries, days


    
if __name__ == '__main__':

    scores, libraries, total_days = read_input(sys.argv[1])
    print(scores)
    for lib in libraries:
        print(lib)
