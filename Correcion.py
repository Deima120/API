import requests

url = "https://api-colombia.com/api/v1/Department"

try: 
    respuesta = requests.get(url, timeout=10) # este es el timepo de respuesta del servidor

    if respuesta.status_code == 200:
        datos = respuesta.json()

        for Departamento in datos:
            nombre = Departamento.get('name', 'Nombre no disponible')
            id = Departamento.get('id', 'id no disponible')
            poblacion = Departamento.get ('population', 'Poblacion no disponible')
            descripcion = Departamento.get('description', 'Descripcion no disponible')
            print(f'El id es: {id} | El nombre es: {nombre} | La poblacion es: {poblacion} | La descripcion es: {descripcion}')

        else:
            print(f'Error en la solicitud: Codigo {respuesta.status_code}')

except requests.exceptions.RequestException as error:
    print(f'Error de conexion: {error}')
