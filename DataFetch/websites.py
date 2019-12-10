from DataFetch.ParkrunResult import ParkrunResult
from DataFetch.soup import get_soup_object, check_existence, get_elements
from DataFetch.urlreader import fetch_HTML

def get_all_parkruns():
    url_base = "https://www.parkrun.pl/gdynia/rezultaty/weeklyresults/?runSeqNumber="
    run_count = 1
    more_runs = True
    while more_runs:
    # The endpoint exists for any number higher then the acutual number of runs -
    # You cannot simply check for an 404 error. It has to check if there is a table with results.
        url = f'{url_base}{run_count}'
        html = fetch_HTML(url)
        soup = get_soup_object(html)
        result_rows = get_elements(soup, ".Results-table-row")
        for row in result_rows:
            result = parkrun_parse_row(row)
        more_runs = check_existence(soup, ".Results-table")
        run_count += 1

def parkrun_parse_row(row):
    position = row.find(class_="Results-table-td--position").get_text()
    name = row.find(class_="Results-table-td--name").find('a').get_text()
    gender = row.find(class_="Results-table-td--gender").find('div').get_text().strip()
    age_group = row.find(class_="Results-table-td--ageGroup").find('a').get_text()
    result = row.find(class_="Results-table-td--time").find('div').get_text()
    return ParkrunResult(position, name, gender, age_group, result)

if __name__ == '__main__':
    get_all_parkruns()
    # get_parkrun("https://www.parkrun.pl/gdynia/rezultaty/weeklyresults/?runSeqNumber=450")
