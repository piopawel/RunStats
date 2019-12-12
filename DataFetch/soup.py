from bs4 import BeautifulSoup

def get_soup_object(html):
    return BeautifulSoup(html, 'lxml')

def check_existence(soup, selector):
    objects = soup.select(selector)
    if objects[0]:
        return True
    return False