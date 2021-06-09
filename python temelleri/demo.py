import requests 
import json
api_url ="https://api.exchangeratesapi.io/latest?base="
bozulan = input("bozulan dovuz turu")
alinan =input("alinan doviz turu")
mik =input(f"ne kadar {bozulan}bozdurmak istiyosun")
requests.get(api_url+bozulan)
result =json.loads(result.text)
print(result)