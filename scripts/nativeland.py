from urllib import response
import requests
import json

response = requests.get('https://native-land.ca/wp-content/themes/Native-Land-Theme/files/indigenousTerritories.json')
data = response.json()

name_slug_list = []

for key in data['features']:
    try:
        name = key['properties']['Name']
        slug = key['properties']['Slug']

        values = {'name': name, 'slug': slug}
        name_slug_list.append(values)
    except KeyError as e:
        print(e.args[0])

# write list to json file
with open('./data/nativeland.json', 'w') as file:
    json.dump(name_slug_list, file)

# Make json prettier
# def print_json(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)
