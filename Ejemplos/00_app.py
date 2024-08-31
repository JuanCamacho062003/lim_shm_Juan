import requests

url = "http://localhost:11434/api/generate"
data = {
    "model": "tinyllama",
    "prompt": "Why is the sky blue?",
    "stream": False
}

# Enviar la solicitud POST
response = requests.post(url, json=data)

# Imprimir el contenido de la respuesta
print(response.text)
