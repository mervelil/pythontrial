
import requests
import json

result =requests.get("https://jsonplaceholder.typicode/todos")
result =json.loads(result.text)
print(result[0])