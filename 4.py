import json

#data = input()
data = '[["a", 1], ["b", 3], ["c", 2]]'
data = json.loads(data)

res = sorted(data, key=lambda x: x[1], reverse=True)
print(res)
