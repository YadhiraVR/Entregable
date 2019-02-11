import requests
import json

# localhost:4000/

#json_string = r.text
#obj = json.loads(json_string) 

#Cargar a un diccionario los datos obtenidos del servidor 


def listar(base_url):
    r = requests.get(base_url + 'score/list')
    #json_string = r.text
    #obj = json.loads(r.text)
    #return obj
    return json.loads(r.text)