import unittest
from unittest.mock import patch

import urlreader
import random
import urllib.error as url_error

class TestUrlReader(unittest.TestCase):

    def test_fetch_response(self):
        response = urlreader.fetch_response("https://www.parkrun.pl/gdynia/rezultaty/weeklyresults/?runSeqNumber=408")
        self.assertEqual(response.code, 200)

        # test a random page number
        random_number = random.randint(0, 400)
        response = urlreader.fetch_response(f'https://www.parkrun.pl/gdynia/rezultaty/weeklyresults/?runSeqNumber={random_number}')
        self.assertEqual(response.code, 200)

    def test__get_HTML_text(self):

        # result, response = urlreader.fetch_HTML("https://www.parkrun.pl/dummy_url")
        # self.assertEqual(response, 404)

        with self.assertRaises(url_error.HTTPError):
            response = urlreader.fetch_response("https://www.parkrun.pl/dummy_url")
            urlreader._get_HTML_text(response)

        with self.assertRaises(ValueError):
            response = urlreader.fetch_response("random_text")
            urlreader._get_HTML_text(response)


if __name__ == '__main__':
    unittest.main()
