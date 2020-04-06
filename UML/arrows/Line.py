import Colors


class Line:
    def __init__(self, firstChart, secondChart, color=Colors.BLACK):
        self.firstChart = firstChart
        self.secondChart = secondChart
        self.color = color
        self.points = list()

    def setFirstPoint(self, coordinates):
        if len(self.points) == 0:
            self.points.append(coordinates)
        else:
            self.points[0] = coordinates

    def setSecondPoint(self, coordinates):
        if len(self.points) == 1:
            self.points.append(coordinates)
        else:
            self.points[len(self.points - 1)] = coordinates
