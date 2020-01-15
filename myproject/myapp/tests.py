# Create your tests here.


# test table sale/client/transfer crud
import requests
from myproject.settings import BASE_ADDRESS

# query
r = requests.post(BASE_ADDRESS + "/myapp/client",     
    json={
    "method": "query",
    "args": {
        "name": "boss",
        # "up_id": 1,
        # "sale_id": 1,
    }
})
print("query:")
print(r.json())

# add
r = requests.post(BASE_ADDRESS + "/myapp/client",     
    json={
    "method": "add",
    "args": {
        "name": "test",
        "phone": "test",
        "passwd": "test",
        "identity": "test",
        "card": "test",
        "up_id": 1,
        # "sale_id": 1,
    }
})
print("add:")
print(r.json())

# update
r = requests.post(BASE_ADDRESS + "/myapp/client",     
    json={
    "method": "update",
    "args": {
        "id": 1,
        "phone": "boss_de_phone",
        # "up_id": 1,
        # "sale_id": 1,
    }
})
print("update:")
print(r.json())




