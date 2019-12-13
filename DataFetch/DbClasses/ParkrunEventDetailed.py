import json
class ParkrunEventDetailed(object):
    def __init__(self, event, results):
        self.event = event
        self.results = results

    def get_details(self):
        event = self.__get_event()
        persons = self.__get_persons()
        results = self.__get_results()
        return event, persons,

    def __get_event(self):
        return json.dumps(self.event)

    def __get_persons(self):
        persons = set()
        for result in self.results:
            persons.add({"name": result.person, "gender": result.gender,"club": result.club})
        return json.dumps(persons)

    def __get_results(self):
        results = set()
        for result in self.results:
            results.add({"event": self.event.number, "person": result.person, "finished": result.finished,
                "age_group": result.age_group, "age_percentage": result.age_percentage, "time": result.time})
        return json.dumps(results)

