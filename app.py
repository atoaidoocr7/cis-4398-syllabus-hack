# API doc https://courses.ianapplebaum.com/public/docs/
import requests

# API SETUP
URL = "https://courses.ianapplebaum.com"
syllabusByIdApi = "/syllabus/"
syllabusApi = "/syllabus/"
userApi = "/user/"
key = "QUtKvrHyNHmaBQAeblqzlBd8BAmyn6HSVNrIfzb8"

headers = {
    'Authorization': "Bearer {QUtKvrHyNHmaBQAeblqzlBd8BAmyn6HSVNrIfzb8}",
    'Content-Type': "application.json",
    'Accept': "application/json"
}

# Get request for api/syllabus/{id}
# Gets a syllabus for a specific semester by (ID)
def getSyllabusById():
    fallSemesterId = "4"                                                                # Seems to be the ID number to return the fall 2023 info
    response = requests.get(URL + syllabusByIdApi + fallSemesterId, headers=headers).json()
    #print(response)
    return response

# Get request for api/syllabus/
# Retrieves every syllabus for every semester
def getSyllabus():
    response = requests.get(URL + syllabusApi, headers=headers).json()
    print(response)

# Get request for api/user/
# Not working yet
def getUser():
    response = requests.get(URL + userApi, headers=headers).json()
    print(response)

# TODO Parse the json here
def parseSyllabus(response):
    print(response)


if __name__ == '__main__':
    response = getSyllabusById()
    parseSyllabus(response)
    #getSyllabus()
    #getUser()


