import pytest
from Funciones import *

@pytest.mark.parametrize("a, b, bolean",[
    (18,3,True),
    (40,5,True),
    (20,3,False),
])
def test_multiple(a,b,bolean):
    if a % b == 0:
        assert multiple(a,b) == bolean

@pytest.mark.parametrize("a, expected",[
    ("44771675", True),
    ("1234567", True),
    ("123456", False),
])
def test_DNI(a,expected):
    if (len(a) == 8) or (len(a) == 7):
        assert validation(a) == expected

@pytest.mark.parametrize("maximum, minimum, expected_average",[
    (30,15,float(22.5)),
    (11,10,float(10.5)),
    (30,10,20),
])
def test_average(maximum,minimum,expected_average):
    assert average(maximum,minimum) == expected_average

@pytest.mark.parametrize("radius, expected_area, expected_perimeter",[
    (12, float(452.39), float(75.4)),
    (20, float(1256.64), float(125.66))
])
def test_area(radius,expected_area,expected_perimeter):
    actual_area = calculate_area(radius)
    actual_perimeter = calculate_perimeter(radius)
    assert actual_area == expected_area
    assert actual_perimeter == expected_perimeter

@pytest.mark.parametrize("user, passw, expected",[
    ("joaquin","abcde",False),
    ("juaneto07","momo",False),
    ("usuario1","asdasd",True),
])
def test_login(user,passw,expected):
    assert login(user,passw) == expected

@pytest.mark.parametrize("value_x, value_y, expected_module",[
    (3,4,5),
    (6,8,10),
    (12,16,20),
])
def test_module(value_x,value_y,expected_module):
    assert module(value_x,value_y) == expected_module

@pytest.mark.parametrize("num, num_factorial",[
    (5,120),
    (7,5040),
    (12, 479001600),
])
def test_factorial(num, num_factorial):
    assert factorial(num) == num_factorial