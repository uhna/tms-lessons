import unittest
from unittest.mock import patch

from unittests.words import join_words, day_of_week, mocked_get
import requests

class TestJoinWords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("A test suite begins")

    def setUp(self):
        print("A test begins")

    def tearDown(self):
        print("A test ends")

    @classmethod
    def tearDownClass(cls):
        print("A test suite ends")

    def test_check_first_word(self):
        print("Test check first word")
        result = join_words("hello", "world")
        self.assertEqual(result, "hello-world")

    def test_check_bool(self):
        print("Test check bool")
        result = join_words("hello", "world", return_bool=True)
        self.assertTrue(result)

    def test_check_hello(self):
        print("Test check hello")
        result = join_words("hello", "world")
        self.assertIn("hello", result, msg=None)

    @unittest.skip("This test invalid")
    def test_skip(self):
        result = join_words("hello", "world")
        self.assertEqual(result, "hello-guys")

    @unittest.skipIf(
        int(day_of_week == "понедельник" or day_of_week == "среда" or
            day_of_week == "пятница"),
        "The test must be skipped on the specified days of the week"
    )
    def test_skip_if(self):
        print("Test check day of week")
        result = join_words("hello", "world")
        self.assertEqual(result, "hello-world")

    @unittest.expectedFailure
    def test_failure(self):
        result = join_words("hello", "world")
        self.assertEqual(result, "hello")

# ==========================================================================

    @patch("requests.get", side_effect=mocked_get)
    def test_mock_google(self, a):
        print ("Test check mock google")
        response = requests.get("https://www.google.com/search?q=badger")
        self.assertEqual(response, "badger-racoon")

    @patch('requests.get')
    def test_google_request(self, mock_get):
        print("Test check status code 404")
        mock_get.return_value.status_code = 404
        response = requests.get('https://www.google.com')
        self.assertEqual(response.status_code, 404)