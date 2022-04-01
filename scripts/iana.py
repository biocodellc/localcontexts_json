import requests
import json

data = requests.get('https://raw.githubusercontent.com/OnroerendErfgoed/language-tags/develop/language_tags/data/json/registry.json').json()

# OUTPUT: [{'tag': 'ru', 'language': ['Russian']}, {'tag': 'ro', 'language': ['Romanian', 'Moldavian', 'Moldovan']}, ]
def list():
    language_list = []

    for item in data:
        if item['Type'] == 'language':
            obj = {'tag': item['Subtag'], 'language': item['Description']}
            language_list.append(obj)

    # write list to json file
    with open('../data/iana.json', 'w') as file:
        json.dump(language_list, file)


# OUTPUT:  {'Russian':'ru', 'Romanian':'to'}
def key_value():
    language_dict = {}
    for item in data:
        if item['Type'] == 'language':
            for lang in item['Description']:
                language_dict[lang] = item['Subtag']

    # write list to json file
    with open('../data/ianaObj.json', 'w') as file:
        json.dump(language_dict, file)