import sys
from typing import List

def get_info(filename : str):

    with open(filename) as f:
        #get the first line of the input
        n = int(f.readline()[:-1])
        print(n)
        photos = []

        k = 0
        for line in f:
            line=line[:-1].split(' ')
            photos.append(Photo(len(photos)), line[0], line[1], set(line[2:]))
        return n, photos

if __name__ == "__main__":
    """
    uso:

    python3 main.py nombre
    """
    filename = sys.argv[1]

    n, phtos = get_info('input/{}.txt'.format(filename))

    with open("{}.out".format(filename), "w") as f:

        for l in results:
            l = list(map(str, l))
            line = str(len(l)) + ' ' + ' '.join(l) + '\n'
            f.write(line)
