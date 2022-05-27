from pprint import pprint
import requests
import json

URL = "http://10.0.0.15:3000/pokemon"

new_pokemon= {
    "name": "Snorlax",
    "number": 143,
    "pokemon_type": "Normal",
    "weaknesses": ["Fighting"],
    "evolutions": ["Munchlax"]
}

new_pokemon= json.dumps(new_pokemon)

resp = requests.post(URL, json=new_pokemon)

response= requests.get(URL).json()



pprint(resp.json())

for x in response:
    print(f"{x['name']} is an awesome Pokemon!  Its number is {x['number']} and its type is: {x['pokemon_type']}\n  Weaknesses include {x['weaknesses']} and evolutions are {x['evolutions']}.\n")
    