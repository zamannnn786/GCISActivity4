import pytest
from polygon import polygon

"""This function will test for correct initialization of Polygon object"""

def test_polygon_initialization():
    testpoly = polygon("Triangle", [3, 3, 3])
    assert testpoly.NameOfPolygon == "Triangle"
    assert testpoly.Sides == [3, 3, 3]

""" This function will test the get_name method"""

def test_get_name():
    testpoly = polygon("Hexagon", [6, 6, 6, 6, 6, 6])
    assert testpoly.get_name() == "Hexagon"

"""This fucntion will test the set_name method"""

def test_set_name():
    testpoly = polygon()
    testpoly.set_name("Pentagon")
    assert testpoly.NameOfPolygon == "Pentagon"

"""This function will test the get_sides method"""

def test_get_sides():
    testpoly = polygon("Square", [4, 4, 4, 4])
    assert testpoly.get_sides() == [4, 4, 4, 4]

"""This function will test the set_sides method"""

def test_set_sides():
    testpoly = polygon()
    testpoly.set_sides([5, 5, 5])
    assert testpoly.Sides == [5, 5, 5]

"""this function tests for equality"""
poly1 = Polygon("Triangle", [3, 3, 3])
poly2 = Polygon("Triangle", [3, 3, 3])
print(poly1 == poly2)  

"""this function tests for inequality"""
poly3 = Polygon("Square", [4, 4, 4, 4])
print(poly1 != poly3) 

#optional
"""this function tests with a non-polygon"""
non_polygon = "Not a polygon"
print(poly1 != non_polygon)


