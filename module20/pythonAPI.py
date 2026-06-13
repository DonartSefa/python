#JSON DATA

# {
#     "name": "Donart",
#     "age": "17",
#     "address" : {
#         "Country": "Kosova",
#         "City": "Prishtine",
#         "ZIP Code": "10000",
#         "Street":"Bajram Bahtiri"
#     },
#     "contacts":[
#         {
#             "type":"email",
#             "value":"donart@gmail.com"
#         },
#         {
#             "type": "phone",
#             "value": "+38345726033"
#         },
#         {
#             "type":"Linkedin",
#             "value":"Donart"
#         }
#     ]
# }


from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {
    "name": "Donart",
    "age": "17",
    "address" : {
        "Country": "Kosova",
        "City": "Prishtine",
        "ZIP Code": "10000",
        "Street":"Bajram Bahtiri"
    },
    "contacts":[
        {
            "type":"email",
            "value":"donart@gmail.com"
        },
        {
            "type": "phone",
            "value": "+38345726033"
        },
        {
            "type":"Linkedin",
            "value":"Donart"
        }
    ]
}