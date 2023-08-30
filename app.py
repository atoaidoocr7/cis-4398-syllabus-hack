
# API doc https://courses.ianapplebaum.com/public/docs/
import requests
import json
from email_server import send_email


class Event:

    def __init__(self, eventId, syllabus_id, event_name, event_description,
                 event_date, created_at, updated_at, class_type):
        self.eventId = eventId
        self.syllabus_id = syllabus_id
        self.event_name = event_name
        self.event_description = event_description
        self.event_date = event_date
        self.created_at = created_at
        self.updated_at = updated_at
        self.class_type = class_type

    def __str__(self):
        formattedStr = ("Event Name: {}\nEvent Description: {}\nCreated At : {}\nUpdated At: {}"
                        ).format(self.event_name, self.event_description, self.created_at, self.updated_at)
        return formattedStr


# Open and read the JSON file
with open('credentials.json', 'r') as json_file:
    data = json.load(json_file)

# API SETUP
URL = "https://courses.ianapplebaum.com"
syllabusByIdApi = "/syllabus/"
syllabusApi = "/syllabus/"
userApi = "/user/"
API_KEY = data['API_KEY']

headers = {
    'Authorization': "Bearer {API_KEY}",
    'Content-Type': "application.json",
    'Accept': "application/json"
}

# Get request for api/syllabus/{id}
# Gets a syllabus for a specific semester by (ID)


def getSyllabusById():
    # Seems to be the ID number to return the fall 2023 info
    fallSemesterId = "4"
    response = requests.get(URL + syllabusByIdApi +
                            fallSemesterId, headers=headers).json()
    # print(response)
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
# Returns an array of event objects


def parseSyllabus(response):

    events = response['events']
    eventObjects = []
    for event in events:
        eventId, syllabus_id, event_name = event['id'], event['syllabus_id'], event['event_name']
        event_desc, event_date, created_at = event["event_description"], event["event_date"], event["created_at"]
        updated_at, class_type = event['updated_at'], event['class_type']

        eventObjects.append(
            Event(eventId, syllabus_id, event_name, event_desc, event_date, created_at, updated_at, class_type))

    for eventObj in eventObjects:
        print(eventObj)
        print("---------------------------\n")
    
    return eventObjects

def formatemail(object):
    message = "Hi,\n\nThis is a reminder that assignment {} is due on {}\n\nAssignment Description: {}\n\nPlease go on your Canvas for more information!".format(object.event_name, object.event_date, object.event_description)

    return message

if __name__ == '__main__':
    response = getSyllabusById()
    eventlist = parseSyllabus(response)
    recipient_list = ['tuo17432@temple.edu', 'tuh18583@temple.edu', 'tul11082@temple.edu', 'tul51449@temple.edu' ]
    send_email("Reminder!", formatemail(eventlist[1]), recipient_list)

    # getSyllabus()
    # getUser()
