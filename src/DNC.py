from point import Point

class DNC:

    order = 2
    iteration = 3
    controlPoints = []

    def __init__(self, O : int, P : list[Point], I : int):
        self.order = O
        self.controlPoints = P
        self.iteration = I
        self.solve()

    def findCurvePoints(self, prevMid : list[Point]):
        mid = [None for i in range (len(prevMid)- 1)]
        for i in range(len(prevMid) - 1):
            mid[i] = Point.midpoint(prevMid[i], prevMid[i+1])

        curve = [None for i in range (len(mid)- 1)]

        for i in range(len(mid) - 1):
            curve[i] = Point.midpoint(mid[i], mid[i+1])

        newMid = [None for i in range (len(curve)+len(mid)+2)]
        newMid[0] = prevMid[0]

        """
        print(len(curve))
        print(len(mid))
        print(len(newMid))
        """

        for i in range(len(mid)):
            newMid[2*i+1] = mid[i]
        for i in range(len(curve)):
            newMid[2*(i+1)] = curve[i]

        newMid[len(newMid)-1] = prevMid[len(prevMid) - 1]
        return curve, newMid
    
    def solve(self):
        midPoints = self.controlPoints
        start = midPoints[0]
        end = midPoints[len(midPoints)-1]
        for i in range(self.iteration):
            curvePoints, midPoints = self.findCurvePoints(midPoints)
            
            for j in range(len(curvePoints)):
                print(str(curvePoints[j].getX()) + " " + str(curvePoints[j].getY()))
                
            # drawCurveFromPoints([start] + curvePoints + [end])