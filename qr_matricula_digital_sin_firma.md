
# Decodificación de un JSON Web Token (JWT) de la Matrícula Digital del Profesional de la Salud

Este repositorio NO OFICIAL contiene un ejemplo de cómo decodificar un JSON Web Token (JWT) utilizado en la Matrícula Digital del Profesional de la Salud en Mi Argentina de la REFEPS.

## Requisitos

Asegúrate de tener Python instalado y la biblioteca `PyJWT`. Puedes instalar `PyJWT` usando pip:

```bash
pip install pyjwt
```

## Ejemplo de Uso

El siguiente script en Python muestra cómo decodificar un JWT sin verificar su firma. Este token contiene información de la matrícula de un profesional de la salud.

```python
import jwt
import base64
import json

# Tu token JWT
# Este es un ejemplo de un token JWT que contiene información codificada.
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
```

### Salida

Al ejecutar el script anterior, deberías obtener una salida similar a la siguiente:

```json
{
  "p": "ProfesionalMatriculaQr(tipoDoc=DNI, numeroDocumento=123456789, nombre=JUAN, apellido=PEREZ, codigo=5410123456789, provincia=CABA, emitidoPor=null, profesion=Médico, matricula=123456, fechaMatricula=01/04/2017, fechaVtoMatricula=28/03/2023, estado=MatriculaEstado(id=1, nombre=Vigente), fechaTitulo=04/02/2014, institucionFormadora=UNIVERSIDAD NACIONAL DE LA MATANZA)"
}
```

## Contribuir

Si deseas contribuir a este repositorio, por favor haz un fork del proyecto y envía un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
