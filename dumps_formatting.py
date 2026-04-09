import json

user = {
    "username": "Nurali",
    "age": 15,
    "active": True
}

print(json.dumps(user, indent=4, ensure_ascii=False))
print(json.dumps(user, indent=2, sort_keys=True, ensure_ascii=False))
