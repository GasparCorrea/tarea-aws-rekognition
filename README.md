# Tarea AWS Rekognition

Gaspar Correa Vergara

# Descripcion

Aplicacion que determina si es que dos imagenes contienen el mismo texto usando [AWS Rekognition](https://console.aws.amazon.com/rekognition/home?region=us-east-1#/text-detection).

# Dependencias

* [boto3](https://pypi.org/project/boto3/) para usar Amazon Web Services.
* datetime para efectos de logging.
* sys para efectos de testeo.

# Instrucciones de uso

El programa debe recibir los siguientes argumentos:
* Bucket: nombre del bucket en el cual se encontraran las imagenes
* Photo control: nombre del archivo de control
* Photo test: nombre del archivo de test
* Expected: resultado esperado del test
* Min Confidence: Confidence minima para aceptar una palabra como reconocida

Ejemplo:

```
python .\compare-text.py tareaps meme-A.jpg meme-B.jpg True 90
```

El output deberia ser el siguiente:

```
2020-11-10 09:26:32.506270 - Bucket: tareaps
2020-11-10 09:26:32.507266 - Photo control: meme-A.jpg
2020-11-10 09:26:32.507266 - Photo test: meme-B.jpg
2020-11-10 09:26:32.507266 - Minimal confidence: 90
2020-11-10 09:26:32.508263 - Detecting text in meme-A.jpg
2020-11-10 09:26:36.334796 - 'como' detected with 99.770% of confidence - Acceptable
2020-11-10 09:26:36.334796 - 'se' detected with 99.043% of confidence - Acceptable
2020-11-10 09:26:36.334796 - 'pone' detected with 99.889% of confidence - Acceptable
2020-11-10 09:26:36.335763 - 'el' detected with 99.579% of confidence - Acceptable
2020-11-10 09:26:36.335763 - 'arroba' detected with 99.883% of confidence - Acceptable
2020-11-10 09:26:36.346739 - Detecting text in meme-B.jpg
2020-11-10 09:26:39.320508 - 'como' detected with 99.715% of confidence - Acceptable
2020-11-10 09:26:39.320508 - 'se' detected with 97.214% of confidence - Acceptable
2020-11-10 09:26:39.321503 - 'pone' detected with 99.986% of confidence - Acceptable
2020-11-10 09:26:39.321503 - 'el' detected with 99.700% of confidence - Acceptable
2020-11-10 09:26:39.321503 - 'arroba' detected with 99.983% of confidence - Acceptable
2020-11-10 09:26:39.324496 - Comparing phrases - True
2020-11-10 09:26:39.324496 - got True, expected True - Test Passed
```