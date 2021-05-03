import requests
import json
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '0885909950805'}
response = requests.get(baseUrl, params=parameters)
content = response.content
info = json.loads(content)
item = info['items']
itemInfo = item[0]
itemCode = itemInfo['ean']
itemName = itemInfo['title']

print(itemCode)
print(itemName)