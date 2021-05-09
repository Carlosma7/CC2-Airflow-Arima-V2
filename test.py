import unittest
import json
import sys, os.path
from servidor import *

class Test_V2(unittest.TestCase): 

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_24h_v2(self):
        response = self.app.get('/servicio/v2/prediccion/24horas')
        self.assertEqual(response.status_code, 200)

    def test_48h_v2(self):
        response = self.app.get('/servicio/v2/prediccion/48horas')
        self.assertEqual(response.status_code, 200)

    def test_72h_v2(self):
        response = self.app.get('/servicio/v2/prediccion/72horas')
        self.assertEqual(response.status_code, 200)