def get_info(filename):
    """
    Function that gets the input
    Return:
        params: A tuple with the input params
        rides: A list with all the rides info
    """
    with open(filename) as f:
        #get the first line of the input
        params = list(map(int, f.readline().split()))

        #list with all the travels
        rides = []

        
        for line in f:

            #Get values from ride line
            ride = list(map(int, line.split()))

            #4-uple with origin and destination in that order
            coordenates = tuple(ride[:4])

            #Earliest step to pick
            earliest = ride[-2]

            #Latest tick to arrive at destination
            latest = ride[-1]

            #List of all rides
            rides.append((coordenates, earliest, latest))


        return params, rides

print(get_info('input/a_example.in'))

data, rides = get_info('input/a_example.in')
rows, columns, nCars, nRides, TIME = data

cars = [Car() for _ in range(nCars)]

results = plan(rides, cars)

with open("results.txt", "w") as f:

    for l in results:
        f.write(' '.join([len(l)]+l))
