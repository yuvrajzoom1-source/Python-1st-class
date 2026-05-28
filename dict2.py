studentdata = {
    "id1":{"name":"sara"},
    "id2":{"name":"david"},
    "id3":{"name":"sara"},
    "id3":{"name":"surya"},
}

result = {}

name = []

for id, data in studentdata.items():

    if data["name"] not in name:

        name.append(data["name"])

        result[id] = data
    
for k,v in result.items():
    print(k,":", v)