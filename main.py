def get_info(filename):

    with open(filename) as f:
        #get the first line of the input
        params = list(map(int, f.readline().split()))

        #list with all the travels
        rides = []

        
        for line in f:
            ride = list(map(int, line.split()))

            coordenates = tuple(ride[:4])
            earliest = ride[-2]
            latest = ride[-1]

            rides.append((coordenates, earliest, latest))


        return params, rides

get_info('a_example.in')
