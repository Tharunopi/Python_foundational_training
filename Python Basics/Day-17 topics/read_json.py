import json

# converting python object to json object is called serialization
data = [
    {"tharun": 89, "atihtys": 87},
    {"goku": 89, "luffy": 87}
]

# serialization
j = json.dumps(data)

path = r"C:\Stack overflow\Python_foundational_training\Python Basics\Day-17 topics\tharun.json"

# with open(path, 'w') as f:
#     f.write(j)

with open(path, 'r') as f:
    data = json.loads(f.read())
    print(data)