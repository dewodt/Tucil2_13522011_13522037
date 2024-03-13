class Point:

    def __init__(self, X, Y):
        self.x = X
        self.y = Y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def midpoint(p : 'Point', q : 'Point') -> 'Point':
        return Point(p.getX() + q.getX() / 2, p.getY() + q.getY() / 2)