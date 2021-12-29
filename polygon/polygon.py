# Objective 1: Create a Polygon Class where initializer takes in the following
# 1. number of edges/vertices
# 2. circumradius
# That can provide these properties:
# 1. edges
# 2. vertices
# 3. interior angle
# 4. edge length
# 5. apothem
# 6. area
# 7. perimeter
# That has these functionalities:
# 1. a proper __repr__ function
# 2. implements equality (==) based on # vertices and circumradius (__eq__)
# 3. implements > based on number of vertices only (__gt__)

# Goal 1: Refactor the `Polygon` class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, \
# but they should not have to get recalculated more than once (since we made our `Polygon` class "immutable").

import math

new_line = "\n"


class Polygon:
    """The class 'Polygon' accepts the number of vertices (greater than or equal to 3) and the circumradius \
    of a polygon as input arguments. The various functions within the class calculate the measures of \
    interior angle, edge length, apothem, area and perimeter for the polygon,to upto two places after decimal."""

    def __init__(self, numberofvertices, circumradius):
        """The initializer function defines that the class accepts two parameters - the number of vertices \
        of the polygon whose properties have to be calculated, and the circumradius of the same. Circumradius \
        is expressed as the radius of an imaginary circle that can be inscribed around the polygon."""

        self.numberofvertices = numberofvertices
        self.circumradius = circumradius

    @property
    def numberofvertices(self):
        return self._numberofvertices

    @numberofvertices.setter
    def numberofvertices(self, nov):
        if (isinstance(nov, int)) == False:
            raise TypeError("Please enter an integer only")
        if (nov < 0):
            raise ValueError("The number of vertices should be a positive value")
        if (nov <= 2):
            raise ValueError("The number of vertices should be greater than or equal to three")

        self._numberofvertices = nov
        self._interiorangle = None
        self._edgelength = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def circumradius(self):
        return self._circumradius

    @circumradius.setter
    def circumradius(self, cr):
        if ((isinstance(cr, int) or isinstance(cr, float)) == False):
            raise TypeError("The value of circumradius should be an int or a float")

        self._circumradius = cr
        self._edgelength = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def interiorangle(self):
        if self._interiorangle is None:
            self._interiorangle = round((self.numberofvertices - 2) * (180/self.numberofvertices), 2)
        return self._interiorangle

    @property
    def edgelength(self):
        if self._edgelength is None:
            self._edgelength = round(2 * self.circumradius * math.sin(math.pi/self.numberofvertices), 2)
        return self._edgelength

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = round(self.circumradius * math.cos(math.pi/self.numberofvertices), 2)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = round(((1/2) * self.numberofvertices * self.edgelength * self.apothem), 2)
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = round((self.numberofvertices * self.edgelength), 2)
        return self._perimeter

    def __repr__(self):
        """The dunder method of representation function describes the messages that are displayed when the class Polygon \
        is called without an argument."""

        return (f'For a polygon with the number of vertices {self.numberofvertices} and a circumradius of {self.circumradius}{new_line}, \
        The measure of interior angle is {self.interiorangle}{new_line}. \
        The measure of edge length is {self.edgelength}{new_line}. \
        The measure of apothem is {self.apothem}{new_line}. \
        The measure of area is {self.area}{new_line}. \
        The measure of perimeter is {self.perimeter}{new_line}')

    def __eq__(self, other):
        """The dunder method of equality has been defined to compare and return with an affirmative when the dimensions - \
        number of vertices and circumradius - of two input polygons are equal."""

        if (self.numberofvertices == other.numberofvertices) and (self.circumradius == other.circumradius):
            return True
        else:
            return False

    def __gt__(self, other):
        """The dunder method of greater than has been defined to compare and return with an affirmative when the number of \
        vertices of one input polygon is greater than the other."""

        if self.numberofvertices > other.numberofvertices:
            return True
        else:
            return False
