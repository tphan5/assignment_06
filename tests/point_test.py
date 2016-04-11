import unittest
import sys
import random
import os

from .. import utils
from .. point import Foo



class TestingPointTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_xyCoordinatesCheck(self):
        points = Foo(4,8)
        self.assertEqual(4,points.x)
        self.assertEqual(8,points.y)

    def test_concidentPoint(self):
        thePoint = Foo(3,8)

        self.assertTrue(thePoint.coincidentPoint((3,8)))
        self.assertFalse(thePoint.coincidentPoint((8,3)))

    def test_shiftPoint(self):
        thePoint = Foo(6,2)
        shiftX = 1
        shiftY = 1
        thePoint.shiftPoint(shiftX,shiftY)
        self.assertEqual((7,3),(thePoint.x, thePoint.y))

    def test_theMarks(self):

        random.seed(88888888)
        marks = ['James', 'Paul', 'Sarah', 'Michael', 'Nancy', 'Henry']
        thePoints = []

        JamesCounter = 0;
        PaulCounter = 0;
        SarahCounter = 0;
        MichaelCounter = 0;
        NancyCounter = 0;
        HenryCounter = 0;

        for i in range(20):
            addPoints = Foo(random.randint(0,9),random.randint(0,9),random.choice(marks))
            thePoints.append(addPoints)
            if thePoints[i].mark == "James":
                JamesCounter = JamesCounter + 1
            elif thePoints[i].mark == "Paul":
                PaulCounter = PaulCounter + 1
            elif thePoints[i].mark == "Sarah":
                SarahCounter = SarahCounter + 1
            elif thePoints[i].mark == "Michael":
                MichaelCounter = MichaelCounter + 1
            elif thePoints[i].mark == "Nancy":
                NancyCounter = NancyCounter + 1
            elif thePoints[i].mark == "Henry":
                HenryCounter = HenryCounter + 1

        self.assertEqual(JamesCounter, 1)
        self.assertEqual(PaulCounter, 5)
        self.assertEqual(SarahCounter, 5)
        self.assertEqual(MichaelCounter, 4)
        self.assertEqual(NancyCounter, 2)
        self.assertEqual(HenryCounter, 3)




