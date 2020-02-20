import sys
from typing import Dict, List
from master import Master
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

def write_output(filename, nlib, lib_books):
    string = ""
    
    string += str(nlib) + "\n"

    for lib in lib_books:
        line1 = f'{lib[0]} {len(lib[1])}\n'
        line2 = " ".join(map(str, lib[1])) + "\n"
        
        string += line1 + line2

    name = filename.replace("input", "output").replace(".txt", ".out")
    with open(name, "w") as f:
        f.write(string)
            
    
if __name__ == '__main__':

    scores, libraries, total_days = read_input(sys.argv[1])
    # print(scores)
    # for lib in libraries:
    #     print(lib)

    m = Master(total_days, scores, libraries)

    rem = m.remaining_days

    while rem != 0:
        rem = m.step()
        

    l, b = m.format_output()
    write_output(sys.argv[1], l, b)
    
