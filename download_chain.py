import requests
import json
import sys

nodeAPI = "http://api.otcgo.cn:10332"

def rpcRequest(method, params):
    return requests.post(nodeAPI, json={"jsonrpc": "2.0", "method": method, "params": params, "id": 0}).json()

def getBlock(index):
    return rpcRequest("getblock", [index,1])

def getBlockCount():
    return rpcRequest("getblockcount", [])

currentBlock = getBlockCount()["result"]

with open(sys.argv[1], "w") as f:
    for i in range(0, currentBlock):
        if i % 10 == 0:
            print(i)
        nextBlock = getBlock(i)
        f.write(json.dumps(nextBlock)+"\n")
