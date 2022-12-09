import json

data = '''
[
    {
        "id" : "007",
        "x" : "2",
        "name" : "Camilo"
    } ,
    {
        "id" : "009",
        "x" : "7",
        "name" : "Paulis"
    }
]
'''
info = json.loads(data)
print('User Count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])