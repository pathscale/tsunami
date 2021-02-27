from wrappers.rapidjson import document as doc

json1 = '{"project":"rapidjson","stars":15,"moons":2,"suns":2}'
json2 = '{"project":"rapidjson","moons":2}'

d1 = doc.Document(json1)
d2 = doc.Document(json2)
d1.set_int("stars", 5)
d2.set_int("moons", 8)
print(d1.get_json())
print(d2.get_json())

d1.set_int("stars", 8)
print(d1.get_json())
print(d1.get_string("project"))
d1.set_string("project", "tsunami")
print(d1.get_string("project"))
d1.set_string("stars", "five")
print(d1.get_string("stars"))
# d1.add_int("dog", 5)
# print(d1.get_int("dog"))
print(d1.get_json())
