from DataFetch.DbClasses import ParkrunEvent
from DataFetch.DbClasses.ParkrunRow import ParkrunRow
from DataFetch.soup import get_soup_object, check_existence
from DataFetch.urlreader import get_HTML

def get_all_parkruns():
    url_base = "https://www.parkrun.pl/gdynia/rezultaty/weeklyresults/?runSeqNumber="
    run_count = 1
    more_runs = True
    while more_runs:
    # The endpoint exists for any number higher then the acutual number of runs -
    # You cannot simply check for an 404 error. It has to check if there is a table with results.
        url = f'{url_base}{run_count}'
        html = get_HTML(url)
        soup = get_soup_object(html)
        event_details = parkrun_parse_row(soup)
        result_rows = soup.select(".Results-table-row")
        for row in result_rows:
            result = parkrun_parse_row(row)
        more_runs = check_existence(soup, ".Results-table")
        run_count += 1

def parkrun_parse_event(page):
    results_header = page.find('Results-header')
    location = results_header.find('h1')
    date = results_header.find('h3').get_text()
    number = results_header.select('span')[1]
    return ParkrunEvent(date, number, location)


def parkrun_parse_row(row):
    name = row['data-name']
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
