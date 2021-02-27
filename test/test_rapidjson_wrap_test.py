import pytest

from core import rapidjson as rj
#from core import tests
from core.cy_tests import tests as tests


def test_documentClassTestNoError():
    json_example = ' { "hello" : "world", "t" : true , "f" : false, "n": null, "i":123, "pi": 3.1416, "a":[1, 2, 3, 4] } '
    d = rj.Document()
    d.Parse(json_example)
    return not d.HasError()


def test_documentClassTestError():
    json_example2 = ' sadas { "hello" : "world", "t" : true , "f" : false, "n": null, "i":123, "pi": 3.1416, "a":[1, 2, 3, 4] } '
    d = rj.Document()
    d.Parse(json_example2)
    if d.HasError() != True:
        assert False, "There should be an error"


def test_documentClassTestError2():
    json_example2 = ' sadas { "hello" : "world", "t" : true , "f" : false, "n": null, "i":123, "pi": 3.1416, "a":[1, 2, 3, 4] } '
    d = rj.Document()
    d.Parse(json_example2)
    print("has: ",d.GetErrorBytes())
    print("got: ",d.GetError())
    print("hard parse: ", rj._text(d.GetErrorBytes()))
    if d.GetError() != "Error(offset 1): Invalid value.":
        assert False, d.GetError()

def test_nogil_test():
    errors, text = tests.run_simple_test()
    text = text
    assert not errors, text