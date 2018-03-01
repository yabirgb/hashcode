
class Car:

    def __init__(self):
        self.position = [0,0]
        self.finishTime = 0

    def getPosition(self):
        return self.position

    def distance(self, p):
        return abs(self.position[0]-p[0])+abs(self.position[1]-p[1])

    def assignRide(self, r):
        self.position = r.getDestination()
        self.finishTime = max(TIME + distance(r.origin), r.getStart()) + r.distance()

    def getFinishTime(self, r):
        return finishTime

