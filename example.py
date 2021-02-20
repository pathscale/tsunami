json_example = ' { "hello" : "world", "t" : true , "f" : false, "n": null, "i":123, "pi": 3.1416, "a":[1, 2, 3, 4] } '
json_example2 = ' sadas { "hello" : "world", "t" : true , "f" : false, "n": null, "i":123, "pi": 3.1416, "a":[1, 2, 3, 4] } '
json_example3 = ' { "hello" : "world", "t" : trueasd , "f" : false, "n": null, "i":123, "pi": 3.1416, "a":[1, 2, 3, 4] } '


import core.wrappers.rapidjson_wrapper.rapidjson as rjw
from core import rapidjson as rj

rjw.test(json_example)
rj.test(json_example)
rj.test(json_example2)
rj.test(json_example3)

d = rj.Document(json_example)
print(d.HasError())

d = rj.Document(json_example2)
print(d.HasError())
print(d.GetError())
