import unittest
import urlreader
import random

class TestUrlReader(unittest.TestCase):

    def test_fetch_HTML(self):
        result, response = urlreader.fetch_HTML("https://www.parkrun.pl/gdynia/rezultaty/weeklyresults/?runSeqNumber=408")
        self.assertEqual(response, 200)
        result, response = urlreader.fetch_HTML("https://www.parkrun.pl/dummy_url")
        self.assertEqual(response, 404)
        # test a random page number
        random_number = random.randint(0, 400)
        result, response = urlreader.fetch_HTML(f'https://www.parkrun.pl/gdynia/rezultaty/weeklyresults/?runSeqNumber={random_number}')
        self.assertEqual(response, 200)

if __name__ == '__main__':
    unittest.main()
