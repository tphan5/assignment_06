from utils import check_coincident


class Foo(object):
    def __init__(self, x, y, mark):
        self.x = x
        self.y = y
        self.mark = mark

    def coincident(self, point1):
        point2 = (self.x, self.y)
        return check_coincident(point1, point2)

    def shift(self,xShift, yShift):
        thePoint = (self.x, self.y)
        self.x, self.y = utils.shift_point(thePoint,xShift,yShift)

from . import utils