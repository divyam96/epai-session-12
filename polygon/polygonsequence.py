# Objective 2: Implement a Custom Polygon sequence type where initializer takes in:
# 1. number of vertices for largest polygon in the sequence
# 2. common circumradius for all polygons
# that can provide these properties:
# max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
# that has these functionalities:
# a. functions as a sequence type (__getitem__)
# b. supports the len() function (__len__)
# c. has a proper representation (__repr__)

# Goal 2: Refactor the `Polygons` (sequence) type, into an **iterable**. Make sure also that the elements in the iterator are computed lazily 
# - i.e. you can no longer use a list as an underlying storage mechanism for your polygons. You'll need to implement both an iterable and an iterator.


from polygon import Polygon


class PolygonSequence:
    """This class creates a sequence of polygons with varying number of vertices and the same circumradius.The least possible \
    number of vertices that a polygon can possess is three. Thus, the indexing of the polygon in the sequence will be initiated \
    in such a way that the 0th element corresponds to 3 and so on. The circumradius is assumed to be the same for all the polygons."""

    def __init__(self, maxvertices, circumradius):
        """The class is initialized in a way that it can accept the arguments of maximum vertices and circumradius."""
        if (isinstance(maxvertices, int)) == False:
            raise TypeError("Please enter an integer only")
        if (maxvertices < 0):
            raise ValueError("TThe max number of vertices should be a positive value")
        if ((isinstance(circumradius, int) or isinstance(circumradius, float)) == False):
            raise TypeError("The value of circumradius should be an int or a float")
        if (circumradius < 0):
            raise ValueError("The value of circumradius should be positive")

        self._maxn = maxvertices
        self._r = circumradius

    def __len__(self):
        """The dunder method of length returns the number of polygons that are present within the sequence."""

        return self._maxn

    def __getitem__(self, s):
        """The dunder method of getitem selects the highest possible index."""

        if isinstance(s, int):
            # single item requested
            if s > (self._maxn - 1):
                raise IndexError
            if s < 0:
                s = self._maxn + s
            if (0 <= s) and (s < 3):
                return None
            return Polygon(s, self._r)
        else:
            # slice being requested
            print(f'requesting [{s.start}:{s.stop}:{s.step}]')
            idx = s.indices(self._maxn)
            rng = range(idx[0], idx[1], idx[2])
            return [Polygon(n, self._r) if n > 2 else None for n in rng]

    def __iter__(self):
        """The dunder method of iteration returns the iterator class, which will make the iteration \
        run till the length of the dataset."""
        return self.PolygonSequenceIterator(self._maxn, self._r)

    def __repr__(self):
        """The dunder method of representation returns the polygon with the maxium number  of vertices and the common circumradius."""

        return (f'This is a PolygonSequence class with polygons upto {self._maxn} vertices and {self._r} circumradius')

    def maximum_efficient_polygon(self):
        """A polygon that has the highest area:perimeter ratio is denoted as the maximum efficiency polygon.\
        This function finds the polygon which has the maximum efficiency among all the others within the sequence."""

        apr_list = [0, 0, 0]
        for idx in range(3, self._maxn):
            p = Polygon(idx, self._r)
            area_perimeter_ratio = p.area / p.perimeter
            apr_list.append(area_perimeter_ratio)
        max_eff = max(apr_list)
        print("Maximum efficient polygon: ", apr_list.index(max_eff))
        print("Max efficiency: ", max_eff)
        return max_eff

    class PolygonSequenceIterator:
        """An iterator is a class which contains both the 'iter' and the 'next' functions, which makes a collection \
        or an iterable indexable. This class has been written as an iterator for the data generated in \
        class PolygonSequence."""

        def __init__(self, maxvertices, circumradius):
            """The class is initialized in a way that it can accept the arguments of maximum vertices and \
            circumradius. In addition, in order to maintain the state of iteration within the collection a \
            variable ‘index’ has been employed, which has been initiated with 0."""
            self.maxvertices = maxvertices
            self.circumradius = circumradius
            self.index = 0

        def __iter__(self):
            """This dunder method of iteration returns the instance of this class (self)."""
            return self

        def __next__(self):
            """This dunder method of next keeps score of the number of times the iteration has been done, \
            and stops the process once of the dataset has been exhausted."""
            if self.index >= self.maxvertices:
                raise StopIteration
            elif 0 <= self.index < 3:
                self.index += 1
                return None
            else:
                result = Polygon(self.index, self.circumradius)
                self.index += 1
                return result
