from urllib import response
import requests
import json

response = requests.get('https://raw.githubusercontent.com/OnroerendErfgoed/language-tags/develop/language_tags/data/json/registry.json')
data = response.json()

language_list = []

for item in data:
    if item['Type'] == 'language':
        for language in item['Description']:
            language_list.append(language)

language_list.sort()

obj = {'languages': language_list}
# write list to json file
with open('../data/iana.json', 'w') as file:
    json.dump(obj, file)