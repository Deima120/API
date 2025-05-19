import requests
import json

url = "https://api-colombia.com/api/v1/TouristicAttraction"

try:
    respuesta = requests.get(url, timeout=10)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        for atraccion in datos:
            nombre = atraccion.get('name', 'Nombre no disponible')
            print(nombre)

    else:
        print(f"Error en la solicitud: Código {respuesta.status_code}")

except requests.exceptions.RequestException as error:
    print(f"Error de conexión: {error}")
