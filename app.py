# API doc https://courses.ianapplebaum.com/public/docs/
import requests

# API SETUP
URL = "https://courses.ianapplebaum.com"
api = "/syllabus/1"
#userHeader = "/api/user"
key = "QUtKvrHyNHmaBQAeblqzlBd8BAmyn6HSVNrIfzb8"

headers = {
    'Authorization': "Bearer {QUtKvrHyNHmaBQAeblqzlBd8BAmyn6HSVNrIfzb8}",
    'Content-Type': "application.json",
    'Accept': "application/json"
}

#Sylabus Get
response = requests.get(URL+api, headers=headers).json()

print(response)
