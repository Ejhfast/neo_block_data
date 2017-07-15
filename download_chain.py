import requests
import json

nodeAPI = "http://api.otcgo.cn:10332"

response = requests.post(nodeAPI, json={"jsonrpc": "2.0", "method": "getblock", "params": [1100000, 1], "id": 0})

print(json.dumps(response.json()))
