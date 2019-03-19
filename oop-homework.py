# class for getting slope and distance between two points
import math

class Line():

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def distance(self):
        return math.sqrt((self.point2[0] - self.point1[0])**2 + (self.point2[1] - self.point1[1])**2)
    
    def slope(self):
        return ((self.point2[1] - self.point1[1])/(self.point2[0] - self.point1[0]))


cord1 = (10, 70)
cord2 = (20,100)

line = Line(cord1, cord2)
print(f'Distance between two point is {line.distance()}')
print(f'Slope between two point is {line.slope()}')