import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self._interior_angle = None
        self._side_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None
        
    def __repr__(self):
        '''represent class'''
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        '''it will count vertices'''
        return self._n
    
    @property
    def count_edges(self):
        '''it will count edges'''
        return self._n
    
    @property
    def circumradius(self):
        '''it will count circumradious'''
        return self._R
    
    @property
    def interior_angle(self):
        '''it will count interior angle'''
        if self._interior_angle is None:
            print('calculating interior angle')
            self._interior_angle = (self._n - 2) * 180 / self._n
        return self._interior_angle

    @property
    def side_length(self):
        '''it will count side length'''
        if self._side_length is None:
            print('calculating side length')
            self._side_length = 2 * self._R * math.sin(math.pi / self._n)
        return self._side_length
    
    @property
    def apothem(self):
        '''it will count apothem'''
        if self._apothem is None:
            print('calculating apothem')
            self._apothem = self._R * math.cos(math.pi / self._n)
        return self._apothem 
    
    @property
    def area(self):
        '''it will count area'''
        if self._area is None:
            print('calculating area')
            self._area = self._n / 2 * self.side_length * self.apothem
        return self._area
    
    @property
    def perimeter(self):
        '''it will count perimeter'''
        if self._perimeter is None:
            print('calculating perimeter')
            self._perimeter = self._n * self.side_length
        return self._perimeter
    
    def __eq__(self, other):
        '''it will give the equality'''
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        '''it will give greater than'''
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented


class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R

    def __len__(self):
        '''return length'''
        return self._m - 2
    
    def __repr__(self):
        '''represent function'''
        return f'Polygons(m={self._m}, R={self._R})'

    def __iter__(self):
        return self.PolygonsIterator(self._R, self._m)

    class PolygonsIterator:
        def __init__(self, r, m):
            self.i = 3
            self.r = r
            self.m = m

        def __iter__(self):
            self

        def __next__(self):
            if self.i<=self.m:
                poly = Polygon(self.i,self.r)
                self.i += 1
                return poly
            else:
                raise StopIteration
    
    def __getitem__(self, s):
        '''it will result the required item at that index'''
        pp = self.PolygonsIterator(self._R,self._m)
        for i in range(s):
            temp = next(pp)
        return temp
    
    @property
    def max_efficiency_polygon(self):
        '''return max efficiency of polygon'''
        sorted_polygons = sorted(self, 
                                 key=lambda p: p.area/p.perimeter,
                                reverse=True)
        return sorted_polygons[0]