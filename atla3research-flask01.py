# This project must include (at least) two (2) scripts. One called alta3research-flask01.py and a second called alta3research-requests02.py

# 1.  Your script alta3research-flask01.py should demonstrate proficiency with the flask library. Ensure your application has:

# at least two endpoints
# at least one of your endpoints should return legal JSON
# has ONE additional feature from the following list:
# one endpoint returns HTML that uses jinja2 logic
# requires a session value be present in order to get a legal response
# writes to/reads from a cookie
# reads from/writes to a sqlite3 database


# 2.  Your script alta3research-requests02.py should demonstrate proficiency with the requests HTTP library. This script should:

# send a GET request to your Flask API; it should target the endpoint that returns legal JSON.
# take the returned JSON and "normalize" it into a format that is easy for users to understand

from flask import Flask
from flask import render_template
from flask import jsonify
import json
from flask import request

app= Flask(__name__)

favorite_pokemons= [{
    "name": "Squirtle",
    "number": 7,
    "pokemon_type": "Water",
    "weaknesses": ["Grass", "Electric"],
    "evolutions": [
        "Wartortle",
        "Blastoise"
              ]
             }]

@app.route("/")  
def get_stats():
    return "Look at me, I am demonstrating proficiency with the flask library!"             

@app.route("/poke/<string:name>")
def cool_pokemon(name):
    return render_template("index.html", pokemon = name)
    
@app.route("/pokemon", methods=["GET", "POST"])    
def get_pokemon():
    if request.method == "POST":
        data = request.json
        if data:
            data= json.loads(data)
            name= data["name"]
            number= data["number"]
            pokemon_type = data["pokemon_type"]
            weaknesses = data["weaknesses"]
            evolutions = data["evolutions"]
            favorite_pokemons.append({"name":name,"number":number,"pokemon_type":pokemon_type,"weaknesses":weaknesses, "evolutions": evolutions})
    return jsonify(favorite_pokemons)
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000) 

 