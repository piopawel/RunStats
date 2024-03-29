import datetime
import json
import re


class ParkrunEventDetailed(object):
    def __init__(self, event, results):
        self.event = event
        self.results = results

    def get_details(self):
        event = self.__get_event()
        persons = self.__get_persons()
        results = self.__get_results()
        return event, persons, results

    def __get_event(self):
        self.event.location = self.event.location.replace('parkrun ', '')
        date = re.sub(r' \| #([0-9]+)', '', self.event.date)
        self.event.date = datetime.datetime.strptime(date, '%d/%m/%Y').strftime("%Y-%m-%d")
        self.event.number = self.event.number.replace(r'#', '')
        return self.event.__dict__

    def __get_persons(self):
        persons = []
        for result in self.results:
            if result.gender == "Kobieta":
                gender = "K"
            else:
                gender = "M"
            persons.append({"name": result.name, "gender": gender, "club": result.club})
        return persons

    def __get_results(self):
        results = []
        for result in self.results:
            results.append({"event": self.event.number, "person": result.name, "finished": result.finished,
                "age_group": result.age_group, "age_percentage": result.age_percentage, "time": result.time})
        return results

