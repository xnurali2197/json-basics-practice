import json

bad = "{'ism':'Nurali'}"

try:
    json.loads(bad)
except json.decoder.JSONDecodeError as e:
    print(e)
