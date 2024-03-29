import json
import os
import time

from DataFetch.DbClasses.ParkrunEvent import ParkrunEvent
from DataFetch.DbClasses.ParkrunEventDetailed import ParkrunEventDetailed
from DataFetch.DbClasses.ParkrunRow import ParkrunRow
from DataFetch.soup import get_soup_object, check_existence
from DataFetch.urlreader import get_HTML

def get_all_parkruns():
    url_base = "https://www.parkrun.pl/gdynia/rezultaty/weeklyresults/?runSeqNumber="
    # run_count = 1
    run_count = 414
    events_dir = os.path.abspath("../WebApp/run_statistics/data")
    persons_dir = os.path.abspath("../WebApp/users/data")
    results_dir = os.path.abspath("../WebApp/base/data")
    while True:
    # The endpoint exists for any number higher then the acutual number of runs -
    # You cannot simply check for an 404 error. It has to check if there is a table with results.
        url = f'{url_base}{run_count}'
        html = get_HTML(url)
        time.sleep((run_count % 5))
        soup = get_soup_object(html)
        if check_existence(soup, ".Results-table tr"):
            event = parkrun_parse_event(soup)
            rows = []
            result_rows = soup.select(".Results-table-row")
            for row in result_rows:
                result = parkrun_parse_row(row)
                if result:
                    rows.append(result)
            event_dict, persons_dict, results_dict = ParkrunEventDetailed(event, rows).get_details()
            save_data(run_count, event_dict, events_dir, persons_dict, persons_dir, results_dict, results_dir)
            run_count += 1
        else:
            break
        # sleep for some time to prevent being blocked

def save_data(file_number, event, event_dir, persons, persons_dir, results, results_dir):
    save_json(event, event_dir, file_number)
    save_json(persons, persons_dir, file_number)
    save_json(results, results_dir, file_number)

def save_json(data, save_dir, file_number):
    with open(os.path.join(save_dir, f'{file_number:04d}.json'), "w", encoding='utf-8') as wf:
        json.dump(data, wf, indent=4, ensure_ascii=False)
        # wf.write(data)


def parkrun_parse_event(page):
    results_header = page.find(class_='Results-header')
    location = results_header.find('h1').get_text()
    date = results_header.find('h3').get_text()
    number = results_header.select('span')[1].get_text()
    return ParkrunEvent(date, number, location)

def parkrun_parse_row(row):
    name = row['data-name']
    if name == "Nieznan(a)y": return

    position = row['data-position']
    age_group = row['data-agegroup']
    age_percentage = row['data-agegrade']
    club = row['data-club']
    gender = row['data-gender']
    result = row.find(class_="Results-table-td--time").find(class_='compact').get_text()
    return ParkrunRow(name, position, age_group, age_percentage, club, gender, result)


if __name__ == '__main__':
    get_all_parkruns()
    # get_parkrun("https://www.parkrun.pl/gdynia/rezultaty/weeklyresults/?runSeqNumber=450")
