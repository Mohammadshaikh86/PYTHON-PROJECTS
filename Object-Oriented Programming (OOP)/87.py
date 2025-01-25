import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Example usage
p1 = Point(1, 2)
p2 = Point(4, 6)
print(f"Distance between points: {p1.distance_from(p2):.2f}")
