from . import utils

class Foo(object):
    def __init__(self, x, y, mark={}):
        self.x = x
        self.y = y
        self.mark = mark

    def coincidentPoint(self, point1):
        point2 = (self.x, self.y)
        return utils.check_coincident(point1, point2)

    def shiftPoint(self,xShift, yShift):
        thePoint = (self.x, self.y)
        self.x, self.y = utils.shift_point(thePoint,xShift,yShift)

