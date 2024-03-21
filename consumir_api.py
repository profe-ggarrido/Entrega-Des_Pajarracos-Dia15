#CODIGO ENTREGADO POR POSTMAN EN LISTA PARA VARIOS LENGUAJE (sector derch Panel)

import requests

def request_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # Manejar el caso de respuesta no exitosa, como levantar una excepción
        raise Exception("Error al obtener la respuesta JSON de la URL:", url)

















# import requests
# from string import Template

# url = "https://www.aves.ninjas.cl/api/birds"

# payload = {}

# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# # print(response.json())
# # print(type(response.json()))

# print(response)
