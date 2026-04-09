import json

data = '{"name":"Nurali","age":15}'
obj = json.loads(data)

print(obj.get("email", "Not accessed"))
print(obj.get("phone"))
