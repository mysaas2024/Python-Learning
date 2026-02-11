import json

x='{"name":"ali","age"18,}'
print(x)
#Converting a Json to a dictionairs
convert=json.loads(x)

#new data
print(convert("name"))