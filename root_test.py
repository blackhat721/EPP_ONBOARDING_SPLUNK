import requests
import json
import pprint
from splunklib import client
import dotenv
import os
dotenv.load_dotenv()

HOST=os.getenv('HOST','')
PORT=os.getenv('PORT','')
USERNAME=os.getenv('USERNAME','')
PASSWORD=os.getenv('PASSWORD','')
BEARER_TOKEN=os.getenv('BEARER_TOKEN','')
response = requests.post("https://localhost:8089/services/authorization/tokens", headers={
    "Authorization": "Bearer eyJraWQiOiJzcGx1bmsuc2VjcmV0IiwiYWxnIjoiSFM1MTIiLCJ2ZXIiOiJ2MiIsInR0eXAiOiJzdGF0aWMifQ.eyJpc3MiOiJhZG1pbiBmcm9tIDUzOGUzYzliOTYyMyIsInN1YiI6ImFkbWluIiwiYXVkIjoidGVzdC1hZG1pbiIsImlkcCI6IlNwbHVuayIsImp0aSI6ImYyY2IwNzFlYzhkYThmZDQwMzgxNWIwZTljN2FjZTFiMjE2ZTRkNWNmMTE4NThhYmExNTBkNDRlMjdkMDJlMjgiLCJpYXQiOjE2OTc1NTI4NTYsImV4cCI6MTcwMDE0NDg1NiwibmJyIjoxNjk3NTUyODU2fQ.5dBefsJ3A3K7uX-04s7-_i0pNwm13wrJZDz2GmGMVzKGlBaHaZdR6razxZPFX4lNJjw0HwHpWwEYs-auyZWHCw",
    "Content-Type": "application/json"
}, data={"name": "admin", "audience": "Testing API", "output_mode": "json" },
    verify=False)

# service = client.connect(
#                         host=HOST,
#                         port=PORT,
#                         splunkToken='eyJraWQiOiJzcGx1bmsuc2VjcmV0IiwiYWxnIjoiSFM1MTIiLCJ2ZXIiOiJ2MiIsInR0eXAiOiJzdGF0aWMifQ.eyJpc3MiOiJhZG1pbiBmcm9tIDUzOGUzYzliOTYyMyIsInN1YiI6ImFkbWluIiwiYXVkIjoiVGVzdGluZyBBUEkiLCJpZHAiOiJTcGx1bmsiLCJqdGkiOiI1NDc1NjRjMmRlOTRjNTllNDU3ZmUzZjkxZTIzYzVkYmUyOTRjMjM3MzU3M2JiYTgxMzg0NWRjOTUwNTE3OWVlIiwiaWF0IjoxNjk3NTY1NjAwLCJleHAiOjE3MDAxNTc2MDAsIm5iciI6MTY5NzU2NTYwMH0.l5fZSuMCfGbljwz72r3q9V_4IXdeYG4H2NAFl9QXoc0IhZuxy7BTeOd7i5CAAR-77pxZvY84bL1FWx0QEqwHFQ')
data = json.loads(response.text)
pp = pprint.PrettyPrinter(indent=4)
token=data['entry'][0]['content']['token']
# pp.pprint()
# print('token: ',token)
# for app in service.apps:
    # print (app.name)