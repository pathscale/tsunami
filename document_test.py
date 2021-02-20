import pytest
from wrappers.rapidjson import document as doc


def test_1():
    json1 = '{"project":"rapid","stars":15,"moons":2,"suns":2}'
    d = doc.Document(json1)
    d.change_json("stars", 5)
    assert d.get_json() == '{"project":"rapid","stars":5,"moons":2,"suns":2}'


def test_2():
    json1 = '{"project":"rapid","stars":15,"moons":2,"suns":2}'
    d = doc.Document(json1)
    d.change_json(dictionary={"stars": 4, "moons": 3, "suns": 81})
    assert d.get_json() == '{"project":"rapid","stars":4,"moons":3,"suns":81}'


def test_3():
    json1 = '{"project":"rapid","stars":15,"moons":2,"suns":2}'
    d = doc.Document(json1)
    d.change_json(valList=["stars", "planets", "moons"], amountList=[5, 2, 30])
    assert d.get_json() == '{"project":"rapid","stars":5,"moons":30,"suns":2}'


def test_4():
    json1 = '{"project":"rapid","stars":15,"moons":2,"suns":2}'
    d = doc.Document(json1)
    d.change_json(tupleList=(["stars", 8], ["moons", 100], ["suns", 0]))
    assert d.get_json() == '{"project":"rapid","stars":8,"moons":100,"suns":0}'


def test_5():
    json1 = '{"project":"rapid","stars":15,"moons":2,"suns":2}'
    d = doc.Document(json1)
    with pytest.raises(TypeError):
        d.change_json()
