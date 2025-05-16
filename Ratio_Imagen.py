""""Crea un programa que se encargue de calcular el aspect ratio de una
    imagen a partir de una url.
    Por ratio hacemos referencia por ejemplo a los "16:9" de una
    imagen de 1920*1080px.
 """""""""

import requests
from PIL import Image
from io import BytesIO
import math

def aspect_ratio_img(url):
    # Descarga la imagen desde la URL
    respuesta = requests.get(url)
    imagen = Image.open(BytesIO(respuesta.content))  # Abre la imagen en memoria

    # Obtiene ancho y alto de la imagen
    ancho, alto = imagen.size

    # Calcula el máximo común divisor 
    divisor = math.gcd(ancho, alto)

    # Calcula la relación simplificada
    ratio_ancho = ancho // divisor
    ratio_alto = alto // divisor

    # Imprime los datos
    print(f"Tamaño de la imagen: {ancho}x{alto} px")
    print(f"Aspect Ratio: {ratio_ancho}:{ratio_alto}")

# URL de ejemplo
url = 'https://images.pexels.com/photos/31986006/pexels-photo-31986006/free-photo-of-encantador-gato-calico-en-un-entorno-urbano.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
# Ejecutar función
aspect_ratio_img(url)
