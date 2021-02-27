import pytest
from wrappers.rapidjson import document as doc


def test_1():
    json1 = '{"project":"rapid","stars":15,"moons":2,"suns":2}'
    d = doc.Document(json1)
    d.set_int("stars", 5)
    assert d.get_json() == '{"project":"rapid","stars":5,"moons":2,"suns":2}'


def test_2():
    json1 = '{"project":"rapid","stars":15,"moons":2,"suns":2}'
    d = doc.Document(json1)
    d.set_int("stars", 5)
    assert d.get_int("stars") == 5


def test_3():
    json1 = '{"project":"rapid","stars":15,"moons":2,"suns":2}'
    d = doc.Document(json1)
    d.set_string("stars", "five")
    assert d.get_string("stars") == "five"


def test_5():
    json1 = '{"project":"rapid","stars":15,"moons":2,"suns":2}'
    d = doc.Document(json1)
    with pytest.raises(TypeError):
        d.set_string()
