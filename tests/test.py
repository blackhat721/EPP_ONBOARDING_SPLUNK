import requests
import json
import pprint
from ..src.splunk_pkg_blackhat721.connection.splunkconnection import SplunkConnection
# from splunk_pkg.src.splunk_pkg_blackhat721.connection import splunkconnection
def token_base_connection():
    response = requests.post("https://localhost:8089/services/authorization/tokens/vivek", headers={
    "Authorization": "Bearer eyJraWQiOiJzcGx1bmsuc2VjcmV0IiwiYWxnIjoiSFM1MTIiLCJ2ZXIiOiJ2MiIsInR0eXAiOiJzdGF0aWMifQ.eyJpc3MiOiJhZG1pbiBmcm9tIDUzOGUzYzliOTYyMyIsInN1YiI6ImFkbWluIiwiYXVkIjoiYWRtaW4tdGVzdCIsImlkcCI6IlNwbHVuayIsImp0aSI6IjdiMTUzMWUzZjk4NmM5ZTUyMDFmY2UxYzk3ZTVhOWU5Y2JkMTRjZTA4YjBkY2M3MTI2YTU2MGZhYjhkNmQzMDYiLCJpYXQiOjE2OTc1NTA4OTEsImV4cCI6MTcwMDE0Mjg5MSwibmJyIjoxNjk3NTUwODkxfQ.Zal4OoCjsXYajsod82h2U4c1eXz-Kjx8C0uwI6elBON5MFvNBgYajdwvtUJg0bEIXTTsnitPjQc3zM2iWtmecQ",
    "Content-Type": "application/json"
    }, data={"name": "vivek", "audience": "Testing API"}, verify=False)

    # print(response.text)
    return response
# Print installed apps to the console to verify login
# for app in service.apps:
    # print app.name
if __name__ == '__main__':
    # response=token_base_connection()
    # data_dict=xmltodict.parse(response.text)
    # print(data_dict)
    # json_data=json.dumps(data_dict)
    # pprint(json_data)
    sc=SplunkConnection()
    sc.connect('admin','admin123',token_authentication=False)
