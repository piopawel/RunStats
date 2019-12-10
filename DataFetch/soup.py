from bs4 import BeautifulSoup

def get_soup_object(html):
    return BeautifulSoup(html, 'lxml')

def get_elements(soup, selector):
    return soup.select(selector)

def check_existence(soup, selector):
    objects = soup.select(selector)
    if objects[0]:
        return True
    return False