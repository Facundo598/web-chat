import requests
from bs4 import BeautifulSoup

# Hacer una solicitud HTTP a la página de Google
url = "https://www.google.com/?hl=es"
response = requests.get(url)

# Verificar que la solicitud se haya realizado con éxito
if response.status_code == 200:
    # Crear un objeto BeautifulSoup para analizar el contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar el elemento del cuerpo (body) y extraer su texto
    body_text = soup.body.get_text()
    
    # Buscar la palabra "Argentina" en el texto del cuerpo
    if "Argentina" in body_text:
        print("Se encontró la palabra 'Argentina' en la página de Google.")
    else:
        print("La palabra 'Argentina' no se encontró en la página de Google.")
else:
    print("Error al hacer la solicitud a la página de Google.")
