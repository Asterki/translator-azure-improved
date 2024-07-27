# Description: This script translates a given text from English to French and Zulu.
# Author: Fernando Rivera
# Asterki Dev "Spark Curiosity" - Microsoft Learn Student Ambassador Program

# Importar las bibliotecas necesarias
import requests  # Esta biblioteca nos ayuda a pedir cosas de internet (APIs)
import uuid  # Esta biblioteca nos ayuda a crear un número único y aleatorio
import json  # Esta biblioteca nos ayuda a trabajar con datos en formato JSON (como un lenguaje que entienden las computadoras)
import dotenv  # Esta biblioteca nos ayuda a usar cosas del sistema, como las variables de entorno
import os  # Esta biblioteca nos ayuda a trabajar con el sistema operativo

config = dotenv.dotenv_values(".env")  # Carga las variables de entorno desde el archivo .env

# Guardar nuestras claves y endpoint del traductor (como nuestras contraseñas secretas)
key = os.environ['TRANSLATOR_TEXT_SUBSCRIPTION_KEY']  # Nuestra clave secreta para usar el traductor
endpoint = os.environ['TRANSLATOR_TEXT_ENDPOINT']  # El lugar en internet donde está el traductor
location = os.environ['TRANSLATOR_TEXT_LOCATION']  # La región donde está nuestro traductor

# Definir el camino donde pedimos la traducción
path = '/translate'  # El camino que sigue nuestra solicitud
constructed_url = endpoint + path  # Juntar el lugar y el camino

# Pedir el lenguaje de entrada y el lenguaje de salida
lenguaje_entrada = input("Ingrese el lenguaje de entrada: ")

# Pedir el lenguaje de salida
lenguaje_salida1 = input("Ingrese el lenguaje de salida1: ")
lenguaje_salida2 = input("Ingrese el lenguaje de salida2: ")

# Pedir el texto a traducir
texto_a_traducir = input("Ingrese el texto a traducir: ")

# Configurar los parámetros de nuestra solicitud
params = {
    'api-version': '3.0',  # La versión de la API (como la versión del juego)
    'from': lenguaje_entrada,  # El idioma del texto original (inglés)
    'to': [lenguaje_salida1, lenguaje_salida2]  # Los idiomas a los que queremos traducir (francés y zulú)
}

# Configurar los encabezados de nuestra solicitud
headers = {
    'Ocp-Apim-Subscription-Key': key,  # Nuestra clave secreta
    'Ocp-Apim-Subscription-Region': location,  # La región de nuestro traductor
    'Content-type': 'application/json',  # El tipo de contenido que estamos enviando
    'X-ClientTraceId': str(uuid.uuid4())  # Un número único y aleatorio para identificar nuestra solicitud
}

# Definir el cuerpo de nuestra solicitud (el texto que queremos traducir)
body = [{
    'text': texto_a_traducir  # El texto que queremos traducir
}]

# Hacer la solicitud de traducción
request = requests.post(constructed_url, params=params, headers=headers, json=body)  # Pedir la traducción
response = request.json()  # Obtener la respuesta en formato JSON

# Mostrar la respuesta de la traducción
print("=============")
for traduccion in response[0]['translations']:
    print(traduccion["to"] + ": " + traduccion["text"])
    print("-----------")