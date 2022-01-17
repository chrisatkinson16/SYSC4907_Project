
import requests
import json
import pprint
import re

url = "https://data.mongodb-api.com/app/data-pydwj/endpoint/data/beta/action/findOne"
payload = json.dumps({
    "collection": "test",
    "database": "SYSC4907",
    "dataSource": "SYSC4907",
    "projection": {
        "_id": 0,
        "messages.payload": 1
    }
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'OGYvBvM9i1fOVwDhJSVZkwJ9WF0VuOpeH0ZhvqV5Ce5UoHi4O2wk8yuXw5VSRrDc'
}
response = requests.request("POST", url, headers=headers, data=payload)

list = response.text.split('{"payload":')
list.remove(list[0])
print ([re.sub('[^a-zA-Z0-9]+', ' ', _) for _ in list])

    
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(list, f, ensure_ascii=False, indent=4)
