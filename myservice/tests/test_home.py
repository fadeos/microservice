import os
import unittest
import json
from myservice.app import app as tested_app
from flask_webtest import TestApp


class TestService(unittest.TestCase):

    def test_home_view(self):
        app = TestApp(tested_app)
        home = app.get('/')
        body = home.json['data']
        self.assertEqual(body, 'test ok')

if __name__ == '__main__':
    unittest.main()
