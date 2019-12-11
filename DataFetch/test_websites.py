import unittest
import websites
import ParkrunResult
import soup
from bs4 import BeautifulSoup
import codecs

class TestWebsites(unittest.TestCase):
    def setUp(self):
        with codecs.open("./test_files/row.html", "r", encoding='utf-8') as rf:
            row_text = rf.read()
            self.row = soup.get_soup_object(row_text)

    def tearDown(self):
        pass

    def test_soup(self):
        self.assertIsInstance(self.row, BeautifulSoup)

    def test_websites(self):
        result = websites.parkrun_parse_row(self.row)
        self.assertEqual(result.position, "1")
        self.assertEqual(result.name, "Waldemar ZABORSKI")
        self.assertEqual(result.gender, "Mężczyzna")
        self.assertEqual(result.age_group, "VM40-44")
        self.assertEqual(result.result, "24:51")

if __name__ == '__main__':
    unittest.main()
