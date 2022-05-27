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
new_hero= json.dumps(new_pokemon)
resp = requests.post(URL, json=new_pokemon)

response= requests.get(URL).json()

pprint(response)
pprint(resp.json())

