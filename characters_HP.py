from urllib import request
import json
import random


#URL variable
URL = "https://hp-api.herokuapp.com/api/characters"


#Function
def character_selection():
    access = request.urlopen(URL)
    response = json.loads(access.read())
    random_characters = random.randint(1,40)
    characters = response[random_characters]
    return f"Who's that Potters, it's {characters['name']}, and here its the image {characters['image']}"

