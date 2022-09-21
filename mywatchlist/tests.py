from django.test import TestCase, Client
from django.urls import resolve
from mywatchlist.views import show_mywatchlist

# Create your tests here.
class AppTest(TestCase):
    def test_html_200(self):
        response = Client().get('https://tugas-2-pbp-majid.herokuapp.com/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_xml_200(self):
        response = Client().get('https://tugas-2-pbp-majid.herokuapp.com/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    def test_json_200(self):
        response = Client().get('https://tugas-2-pbp-majid.herokuapp.com/mywatchlist/json/')
        self.assertEqual(response.status_code,200)