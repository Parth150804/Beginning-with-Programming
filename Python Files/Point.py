class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return ((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2) ** 0.5

    def distance(self, point):
        return abs((self.p2.y - self.p1.y) * point.x - (self.p2.x - self.p1.x) * point.y + self.p2.x * self.p1.y - self.p2.y * self.p1.x) / self.length()

    def distance_seg(self, segment):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = segment.p1.x, segment.p1.y
        x4, y4 = segment.p2.x, segment.p2.y

        denominator = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
        if denominator == 0:
            return None

        ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denominator
        ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denominator

        if 0 <= ua <= 1 and 0 <= ub <= 1:
            x = x1 + ua * (x2 - x1)
            y = y1 + ua * (y2 - y1)
            return ((x - x3) ** 2 + (y - y3) ** 2) ** 0.5
        else:
            return None


a = Point(1, 2)
b = Point(1, 4)

line = Segment(a, b)

print(line.length())
print(line.distance(a))
