import requests
from string import Template

from consumir_api import request_json

# Obtener los datos de la API de aves
url = "https://www.aves.ninjas.cl/api/birds"
response = request_json(url)

# Crear una lista de tuplas con la imagen, nombre en español y enlace de cada ave
lista_img = [(elemento['images']['main'], elemento['name']['spanish'], elemento['_links']['self'], elemento['name']['english'], elemento['name']['latin']) for elemento in response]

# Plantilla para la estructura de la tarjeta (card)
nuevo_card = """
<div class="col-md-4 col-lg-3 mb-4">
    <div class="card">
        <img src="$url" class="card-img-top" alt="...">
        <div class="card-body">
            <h5 class="card-title">$title</h5>
            
            <p class="card-text card-text-spanish"><u>Nombre en español:</u> $name_es</p>
            <p class="card-text">Nombre en inglés: $name_en</p>
            <p class="card-text">Nombre latino: $name_latin</p>
            <a href="$link" class="btn btn-primary">Ver más</a>
        </div>
    </div>
</div>
"""

# Crear la plantilla de la tarjeta
img_template = Template(nuevo_card)
texto_img = ''

# Generar las tarjetas para cada ave
for img, name_es, link, name_en, name_latin in sorted(lista_img, key=lambda x: x[2]):  # Ordenar por el enlace (orden)
    texto_img += img_template.substitute(url=img, title=name_es, name_es=name_es, name_en=name_en, name_latin=name_latin, link=link) + '\n'

# Plantilla HTML principal
html_template = Template('''<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Desafío Aves</title>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="styles.css">
                         
    <style>
    .card-text-spanish {
      text-decoration: underline;
    }
  </style>
</head>
<body>
    <h1><center>PAJARRACOS DE CHILE</center></h1>

    <div class="container">
        <div class="row">
            $body
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
''')

# Insertar las tarjetas en la plantilla HTML
html = html_template.substitute(body=texto_img)

# Escribir el archivo HTML
with open('index.html', 'w+', encoding='utf-8') as archivo:
    archivo.write(html)

print("*************************** game over ***************************")
