import json

user = {
    "username": "Nurali",
    "age": 15,
    "active": True,
    "location": None,
    "hobbies": ["playing football", "coding"]
}

print(json.dumps(user))
print(type(json.dumps(user)))
