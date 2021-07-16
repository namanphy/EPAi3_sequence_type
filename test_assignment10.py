import Assignment10
from Assignment10 import Polygon
from Assignment10 import Polygons
import os
import inspect
import re
import math


README_CONTENT_CHECK_FOR = [
'Polygon', 
'repr', 
'interior angle', 
'side length', 
'apothem',
'area', 
'perimeter', 
'eq', 
'gt', 
'Polygons', 
'len', 
'iter', 
'PolygonsIterator',
]



def test_readme_exists():
    assert os.path.isfile("readme.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("readme.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 250, "Make your README.md file interesting! Add atleast 300 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("readme.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("readme.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 8

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(Assignment10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001
    
    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass
                       
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.count_vertices == n, (f'actual: {p.count_vertices},'
                                   f' expected: {n}')
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')
    
    assert math.isclose(p.side_length, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.side_length},'
                                          f' expected: {math.sqrt(2)}')
    
    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
    
    assert math.isclose(p.apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          ' expected: 0.707')
    p = Polygon(6, 2)
    assert math.isclose(p.side_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p = Polygon(12, 3)
    assert math.isclose(p.side_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)
    
    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5


def test_polygon_repr():
    p = Polygon(7,10)
    assert p.__repr__() == 'Polygon(n=7, R=10)','repr function did not match'

def test_count_vertices():
    p = Polygon(7,10)
    assert p.count_vertices == 7,'did not match'

def test_count_edges():
    p = Polygon(7,10)
    assert p.count_edges == 7,'did not match'

def test_circumradius():
    p = Polygon(7,10)
    assert p.circumradius == 10,'did not match'

def test_interior_angle():
    p = Polygon(7,10)
    assert p.interior_angle == 128.57142857142858,'did not match'

def test_side_length():
    p = Polygon(7,10)
    assert p.side_length == 8.677674782351163,'did not match'

def test_apothem():
    p = Polygon(7,10)
    assert p.apothem == 9.009688679024192,'did not match'

def test_area():
    p = Polygon(7,10)
    assert p.area == 273.6410188638105,'did not match'

def test_perimeter():
    p = Polygon(7,10)
    assert p.perimeter == 60.74372347645814,'did not match'

def test_polygons_len():
    pp = Polygons(7,10)
    assert pp.__len__() == 5,'length did not match'

def test_polygons_repr():
    pp = Polygons(7,10)
    assert pp.__repr__() == 'Polygons(m=7, R=10)','repr function did not match'

def test_polygons_getitem():
    pp = Polygons(7,10)
    assert pp.__getitem__(3) == Polygon(n=5, R=10),'did not work'

def test_polygons_max():
    pp = Polygons(7,10)
    assert pp.max_efficiency_polygon == Polygon(n=7, R=10),'did not work'