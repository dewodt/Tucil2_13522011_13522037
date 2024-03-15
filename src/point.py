class Point:
    x: float
    y: float

    def __init__(self, X: float, Y: float):
        self.x = X
        self.y = Y

    def getX(self) -> float:
        return self.x

    def getY(self) -> float:
        return self.y

    def print(self):
        print(f"({self.x}, {self.y})")

    @staticmethod
    def midpoint(p: "Point", q: "Point") -> "Point":
        return Point(((p.getX() + q.getX())) / 2.0, ((p.getY() + q.getY())) / 2.0)
