import os
import unittest
from app import app
from mockupdb import go, Command, MockupDB  
from pymongo import MongoClient


# Test setup for connecting to a mock server
class MockupDBFlaskTest(unittest.TestCase):

    def setUp(self):
        self.server = MockupDB(auto_ismaster=True)
        self.server.run()
        # create mongo connection to mock server

        app.testing = True

        # takes actual Mongo Uri for use in mock server
        app.config['TESTING'] = True
        app.config['MONGO_URI'] = self.server.uri
        self.app = app.test_client()

    def tearDown(self):
        self.server.stop()

    def test_main_page(self):
        response = self.app.get('/get_products', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()

