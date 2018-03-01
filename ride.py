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
        return self.endTime    
        
        
    def obsolete(self, currentTime):
        return currentTime + self.distance() >= self.finish
