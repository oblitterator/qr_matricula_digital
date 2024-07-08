import jwt
import base64
import json

# Tu token JWT
# Este es un ejemplo de un token JWT.
token = 'eyJ1eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwIjoiUHJvZmVzaW8uYWxNYXRyaWN1bGFRcih0aXBvRG9jPUROSSwgbnVtZXJvRG9jdW1lbnRvPTMzNjQyMjExLCBub21icmU9RlJBTkNJU0NPLCBhcGVsbGlkbz1EVVJFLCBjb2RpZ289NTQxMDMzNjQyMjExLCBwcm92aW5jaWE9Q0FCQSwgZW1pdGlkb1Bvcj1udWxsLCBwcm9mZXNpb249TcOpZGljbywgbWF0cmljdWxhPTE3MDg0NiwgZmVjaGFNYXRyaWN1bGE9MDEvMDQvMjAxOSwgZmVjaGFNYXRyaWN1bGE9MjgvMDIvMjAyNSwgZXN0YWRvPU1hdHJpY3VsYUVzdGFkbyhpZD0xLCBub21icmU9VmlnZW50ZSksIGZlY2hhVGl0dWxvPTA0LzAyLzIwMTksIGluc3RpdHVjaW9uRm9ybWFkb3JhPVVOSVZFUlNJREFEIE5BQ0lPTkFMIERFIExBIE1BVEFOWkEpIn0.IJwQI_pIpPmanMn2J5PNEtZGTmqYyWd9eMnf0R1eOWE'

# Dividir el token en sus componentes
# Un token JWT tiene tres partes: el encabezado, el payload y la firma, separados por puntos.
header, payload, signature = token.split('.')

# Decodificar el payload
# El payload es la parte del token que contiene la información. Está codificado en Base64.
payload_decoded = base64.urlsafe_b64decode(payload + '==')

# Convertir el payload decodificado de bytes a un diccionario JSON
decoded_token = json.loads(payload_decoded)

# Imprimir el token decodificado
# Esto mostrará la información contenida en el payload del JWT.
print(decoded_token)
