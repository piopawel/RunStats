import json


class Event(object):
    def __init__(self, date, number, location):
        date = date
        number = number
        location = location

    def get_json(self):
        return json.dumps(self)