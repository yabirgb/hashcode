def get_info(filename):

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

print(get_info('a_example.in'))

class Ride():

    def __init__(self, data):
        self.origin = data[0][:2]
        self.destination = data[0][2:4]
        self.start = data[1]
        self.finish = data[2] #The latest
        self.endTime = self.start + self.distance()

    def getDestination(self):
        """
        Get the start position for a ride.
        Return:
            A tuple (a,b)
        """
        
        return self.destination

    def getOrigin(self):
        """
        Get the start position for a ride.
        Return:
            A tuple (a,b)
        """
        return self.origin

    def getStart(self):
        """
        Get the start tick (time)
        Return:
            a integer
        """
        return self.start

    def distance(self):
        """
        Distance between point (a,b) the origin and 
        (x,y) the destination
        Return:
            int with the total distance
        """

        return abs(self.origin[0]-self.destination[0]) + abs(self.origin[1] - self.destination[1])

    def getEnd(self):
        return self.start +
        
        
        
