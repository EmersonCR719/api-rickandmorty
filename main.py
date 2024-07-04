import requests
import json


# Requests simple
url = 'https://rickandmortyapi.com/api/character/2'
# r = requests.get(url)
# j = r.json()

# status = j['status']


# Obtener los nombres y el status de todos los personajes de la serie en un diccionario {id : {status : name}}
# Tarde aproximadamente 6:50.591s en obtenerlos <|:,v
def characters():

    index = 1 
    dict_characters = {}

    while True:
        url = f'https://rickandmortyapi.com/api/character/{index}'
        r = requests.get(url)
        if r.status_code == 404:   # Manejo del error cuando el personaje no se encuentra
            break
        j = r.json()
        name = j['name']
        status = j['status']
        dict_characters[index] = {'name' : name, 'status' : status}  # Actualiza el diccionario con el nuevo personaje
        index += 1

    return dict_characters


# Requests: Lista de episodios
def episodes():
    index = 1
    list_espisodes = list()
    while True:
        url = f'https://rickandmortyapi.com/api/episode/{index}'
        r = requests.get(url)
        if r.status_code == 404:
            break
        j = r.json()
        list_espisodes.append(j['episode'])
        index += 1
    return list_espisodes


# Request: Personajes por especie
def fetch_characters_by_species(species):

    url = f'https://rickandmortyapi.com/api/character/?species={species}'
    response = requests.get(url)
    data = response.json()
    
    characters = []
    
    while data['info']['next']:
        characters.extend(data['results'])
        response = requests.get(data['info']['next'])
        data = response.json()
    
    characters.extend(data['results'])
    
    return characters


print(fetch_characters_by_species('Human'))



