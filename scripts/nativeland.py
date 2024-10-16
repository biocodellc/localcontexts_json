from urllib import response
from pathlib import Path
import requests
import json
import os


def download_artifacts():
    native_land_api_key = os.getenv('NATIVELAND_API_KEY')

    if native_land_api_key is None:
        raise Exception('NATIVELAND_API_KEY environment variable is not defined')

    response = requests.get(
        f'https://native-land.ca/api/polygons/geojson/territories?key={native_land_api_key}'
    )
    data = response.json()

    slug_name_list = []
    slug_coordinates_description_dict = {}

    for key in data['features']:
        try:
            name = key['properties']['Name']
            slug = key['properties']['Slug']
            description = key['properties']['description']
            coordinates = key['geometry']['coordinates']

            # omit recording slug data when it's missing coordinates
            if len(coordinates) == 0 or len(coordinates[0]) == 0 or len(coordinates[0][0]) == 0:
                continue

            slug_name_list.append(
                {'slug': slug, 'name': name}
            )
            slug_coordinates_description_dict[slug] = {
                'coordinates': coordinates, 'description': description
            }
        except KeyError as e:
            print(e.args[0])

    current_file_path = os.path.abspath(__file__)
    repo_folder = str(
        Path(current_file_path).parent.parent
    )

    # write nativeland_slug_name_list to json file
    slug_name_list_file_path = os.path.join(
        repo_folder,
        'data',
        'nativeland_slug_name_list.json'
    )
    with open(slug_name_list_file_path,'w') as file:
        json.dump(slug_name_list, file)

    # write slug_coordinates_description_dict to json file
    slug_coordinates_description_dict_file_path = os.path.join(
        repo_folder,
        'data',
        'nativeland_slug_coordinates_description_dict.json'
    )
    with open(slug_coordinates_description_dict_file_path, 'w') as file:
        json.dump(slug_coordinates_description_dict, file)


if __name__ == '__main__':
    download_artifacts()
