import math
from heapq import heappush, heappop

def distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]- p2[1])

def score_car(x, rides):
    time = 0
    pos = [0,0]
    score = 0
    for n in x:
        time+=distance(pos, rides[n].getOrigin())
        pos = rides[n].getDestination()
        if time <= rides[n].getStart():
            time = rides[n].getStart()
            score+=BONUS
        if time+rides[n].distance()<ride[n].getEnd():
            score+=rides[n].distance()
        time+=rides[n].distance()

    return score

def plan(rides, cars, bonus, TIME, maxDistance):
    time = 0
    pending_rides = [x for x in range(len(rides))]
    #pending_rides.sort(key=lambda x: rides[x].distance(), reverse = True)
    available_cars = [x for x in range(len(cars))]
    busy_cars = []

    results = [[] for _ in cars]
    while time < TIME and pending_rides:

        while busy_cars:
            car = heappop(busy_cars)
            if car[0] != time:
                heappush(busy_cars, car)
                break
            available_cars.append(car[1])


        pending_rides.sort(key=lambda x: maxDistance if (rides[x].getEnd() == time) else 1/(rides[x].getEnd() - time), reverse = True)
        while pending_rides and available_cars:
   
            min_d = maxDistance
            assigned_car = 0
            for car in available_cars:
                if min_d > distance(cars[car].getPosition(), rides[pending_rides[0]].getOrigin()):
                    min_d = distance(cars[car].getPosition(), rides[pending_rides[0]].getOrigin())
                    assigned_car = car

            cars[assigned_car].assignRide(rides[pending_rides[0]], time)
            
            results[assigned_car].append(pending_rides[0])
            pending_rides.pop(0)
            heappush(busy_cars, (cars[assigned_car].getFinishTime(), assigned_car))
            available_cars.remove(assigned_car)

            while pending_rides and rides[pending_rides[0]].obsolete(time):
                pending_rides.pop(0)
            
        time = min(busy_cars)[0]

    return results
