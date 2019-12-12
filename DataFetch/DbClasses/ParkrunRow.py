import json


class ParkrunRow(object):
    def __init__(self, name, finished, age_group, age_percentage, club, gender, time):
        self.name = name
        self.finished = finished
        self.age_group = age_group
        self.age_percentage = age_percentage
        self.club = club
        self.gender = gender
        self.time = time

    def get_json(self):
        return json.dumps(self)
