import pytest
from Funciones import *

# def validartion (Nombre de la funcion a que corresponde este test)
@pytest.mark.parametrize("a, expected",[
    ("44771675", True),
    ("1234567", True),
    ("123456", False),
])
def test_DNI(a,expected):
    assert validation(a) == expected

# def lastword
@pytest.mark.parametrize("long, expectedlong",[
    ("hola que tal",3),
    ("programar en python",6),
])
def test_lastword(long, expectedlong):
    assert lastword(long) == expectedlong

# def name
@pytest.mark.parametrize("totalname, position, expectedname", [
    ("Juan Alberto Contreras",0,"Juan"),
    ("Juan Alberto Contreras",-1,"Contreras"),
])
def test_name(totalname, position, expectedname):
    assert name(totalname, position) == expectedname

# def user
@pytest.mark.parametrize("name, surname, DNI, expectedusername",[
    ("Valentin","Curiel","44771675","Valentin6447")
])
def test_user(name,surname,DNI,expectedusername):
    assert user(name,surname,DNI) == expectedusername

# def multiple
@pytest.mark.parametrize("a, b, bolean",[
    (18,3,True),
    (40,5,True),
    (20,3,False),
])
def test_multiple(a,b,bolean):
        assert multiple(a,b) == bolean

# def average
@pytest.mark.parametrize("maximum, minimum, expected_average",[
    (30,15,float(22.5)),
    (11,10,float(10.5)),
    (30,10,20),
])
def test_average(maximum,minimum,expected_average):
    assert average(maximum,minimum) == expected_average

# def intespace
@pytest.mark.parametrize("word, expectedword",[
    ("Hola,tu","H o l a , t u "),
])
def test_interspace(word, expectedword):
    assert interspace(word) == expectedword

# def maxnumber
@pytest.mark.parametrize("numbers, maxnum",[
    ([1,2,3,4,5],5),
])
def test_maxnumber(numbers, maxnum):
    assert maxnumber(numbers) == maxnum

# def minnumber
@pytest.mark.parametrize("numbers, minnum",[
    ([3,4,5,2,1],1),
])
def test_minnumber(numbers, minnum):
    assert minnumber(numbers) == minnum

#def calculate_area y def calculate_perimeter
@pytest.mark.parametrize("radius, expected_area, expected_perimeter",[
    (12, float(452.39), float(75.4)),
    (20, float(1256.64), float(125.66))
])
def test_area(radius,expected_area,expected_perimeter):
    actual_area = calculate_area(radius)
    actual_perimeter = calculate_perimeter(radius)
    assert actual_area == expected_area
    assert actual_perimeter == expected_perimeter

#def login
@pytest.mark.parametrize("user, passw, expected",[
    ("joaquin","abcde",False),
    ("juaneto07","momo",False),
    ("usuario1","asdasd",True),
])
def test_login(user,passw,expected):
    assert login(user,passw) == expected

# def discount
@pytest.mark.parametrize("shoppinglist, expectedprice",[
    ({1000:50, 700:40, 2650:25},2907.5)
])
def test_discount(shoppinglist,expectedprice):
    assert discount(shoppinglist) == expectedprice

# def change_list
@pytest.mark.parametrize("list_1, expectedlist_1",[
    (["hola","que","tal"],["tal","que","hola"]),
])
def test_changelist(list_1, expectedlist_1):
    assert change_list(list_1) == expectedlist_1

# def reverse_list
@pytest.mark.parametrize("list_2, expectedlist_2",[
    (["hola","que","tal"],["tal","que","hola"]),
])
def test_reverselist(list_2,expectedlist_2):
    assert reverse_list(list_2) == expectedlist_2

# def dictionary_speech
@pytest.mark.parametrize("words, numletters",[
    ("programo en python", {"programo":8, "en":2, "python":6}),
])
def test_dictionary_speech(words, numletters):
    assert dictionary_speech(words) == numletters

# def module
@pytest.mark.parametrize("value_x, value_y, expected_module",[
    (3,4,5),
    (6,8,10),
    (12,16,20),
])
def test_module(value_x,value_y,expected_module):
    assert module(value_x,value_y) == expected_module

# def prime_numbers
@pytest.mark.parametrize("number, expectedboolean",[
    (2, True),
    (12, False),
    (29, True),
    (25, False),
])
def test_prime_numbers(number, expectedboolean):
    assert prime_numbers(number) == expectedboolean

# def factorial
@pytest.mark.parametrize("num, num_factorial",[
    (5,120),
    (7,5040),
    (12, 479001600),
])
def test_factorial(num, num_factorial):
    assert factorial(num) == num_factorial

# def digit_in_number
@pytest.mark.parametrize("number, digitnumber, frecuency",[
    (123123123,1,3),
    (223334446666656,6,6),
])
def test_digit_in_number(number, digitnumber, frecuency):
    assert digit_in_number(number,digitnumber) == frecuency

# def digits_addition
@pytest.mark.parametrize("number, expected_addition",[
    (12,3),
    (246,12),
])
def test_digits_addition(number, expected_addition):
    assert digits_addition(number) == expected_addition

# def bigger
@pytest.mark.parametrize("number, maxnumber",[
    (3,3),
    (5,5),
    (4,5),
    (6,6),
    (5,6),
])
def test_bigger(number, maxnumber):
    assert bigger(number) <= maxnumber