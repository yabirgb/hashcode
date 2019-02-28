import sys
from photo import Photo
from evolution import Evolution
from individual import Individual

def get_info(filename):

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

    python3 main.py nombre-entrada
    """
    filename = sys.argv[1]

    n, photos = get_info('input/{}.txt'.format(filename))

    e = evolution.Evolution(50, photos)

    for _ in range(50):
        e.run_generation()

    best = e.best_ever()
    
    with open("{}.out".format(filename), "w") as f:

        f.writeline(len(best.slides))
        for s in best.slides:
            f.writeline(' '.join(list(map(str,best.photos))))
            line = str(len(l)) + ' ' + ' '.join(l) + '\n'
            f.write(line)
