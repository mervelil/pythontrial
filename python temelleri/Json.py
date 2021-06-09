#dictionaryß
import json
#person_str ="{"name":"ali","language":["python","c"]}"
"""
result=person["name"]
result=person["language"]
print(result)
"""
with open ("person.json") as f:
    data =json.load(f)
    print(data["name"])
    print(data["language"])
result =json.loads(person_str)
result=result["name"]
print(result)
#dicto to json str
result =json.dumps(person_str)
prinT (result)