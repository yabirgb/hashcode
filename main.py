from car import Car
from plan import *
from ride import Ride

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

data, ridesRaw = get_info('input/a_example.in')
rows, columns, nCars, nRides, bonus, TIME = data

cars = [Car() for _ in range(nCars)]
rides = [Ride(elem) for elem in ridesRaw]
maxDistance = rows + columns

results = plan(rides, cars, bonus, TIME, maxDistance)


with open("results.txt", "w") as f:

    for l in results:
        l = list(map(str, l))
        line = str(len(l)) + ' ' + ' '.join(l) + '\n'
        f.write(line)
