import json

json_data = '{"name":"Nurali", "age":15, "active":true}'
obj = json.loads(json_data)

print(obj)
print(obj["name"])
