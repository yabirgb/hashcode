from ride.py import Ride
class Car:

    def __init__(self):
        self.position = [0,0]
        self.finishTime = 0

    """
    Current position of the car (tuple)
    """
    def getPosition(self):
        return self.position

    """
    Distance to the point given
    The point must be given as a tuple
    """
    def distance(self, p):
        return abs(self.position[0]-p[0])+abs(self.position[1]-p[1])

    """
    Update the attributes of the car as it takes the ride given
    """
    def assignRide(self, r, time):
        self.position = r.getDestination()
        self.finishTime = max(time + distance(r.origin), r.getStart()) + r.distance()

    """
    Time when the car will be free again
    """
    def getFinishTime(self):
        return finishTime
