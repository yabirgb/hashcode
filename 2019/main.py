import sys
from photo import Photo
from evolution import Evolution
from individual import Individual

population = int(sys.argv[2])
generations = int(sys.argv[3])
mutate_vertical_percent = float(sys.argv[4])
mutate_random_percent = float(sys.argv[5])
parent_percent = float(sys.argv[5])

def get_info(filename):

    with open(filename+".txt") as f:
        #get the first line of the input
        n = int(f.readline()[:-1])
        
        photos = []
        verticals = 0
        
        for line in f:
            line=line[:-1].split(' ')
            
            if line[0] == 'V':
                verticals+=1
            
            photos.append(Photo(len(photos), line[0], set(line[2:])))
        return n, photos, verticals
    
if __name__ == "__main__":
    """
    uso:

    python3 main.py nombre-entrada
    """
    filename = sys.argv[1]

    n, photos, verticals = get_info('input/{}'.format(filename))
    print("file " + filename)
    e = Evolution(population, photos)
    if verticals <=1:
        vertical_mutation = 0
    else:
        vertical_mutation = mutate_vertical_percent
    
    e.init_params(vertical_mutation, mutate_random_percent, parent_percent)
    
    for i in range(generations):
        print ("generation "+ str(i))
        e.run_generation()

    best = e.best_ever

    fingerprint = "{}-{}-{}-{}-{}".format(population,generations, mutate_vertical_percent, mutate_random_percent, parent_percent )
    with open("output/{}-{}.out".format(filename, fingerprint), "w") as f:

        f.write(str(len(best.slides)) + '\n')
        for s in best.slides:
            pks = [x.pk for x in s.photos if x != None]
            f.write(' '.join(list(map(str,pks)))+'\n')
