from wrappers.rapidjson import document as doc

json1 = '{"project":"rapidjson","stars":15,"moons":2,"suns":2}'
json2 = '{"project":"rapidjson","moons":2}'

d1 = doc.Document(json1)
d2 = doc.Document(json2)
d1.change_json("stars", 5)
d2.change_json("moons", 8)
print(d1.get_json())
print(d2.get_json())

d1.change_json("stars", 8)
print(d1.get_json())

d1.change_json(dictionary={"stars": 4, "moons": 3, "suns": 81})
print(d1.get_json())

d1.change_json(valList=["stars", "planets", "moons"], amountList=[5, 2, 30])
print(d1.get_json())

d1.change_json(tupleList=(["stars", 8], ["moons", 100], ["suns", 0]))
print(d1.get_json())
