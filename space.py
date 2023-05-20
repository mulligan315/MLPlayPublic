import requests

response = requests.get("http://api.open-notify.org/astros.json")
space_json= response.json()
#print(space_json)

people = space_json['people']
for person in people:
    print(person['name'],person['craft'])