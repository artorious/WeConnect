#!/usr/bin/env python3

from app import app

import unittest

class SimpleTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_index_http_method(self):
        response = self.app.get('/')
        self.assertIn('GET', str(response.data))

    def test_index_http_response_status(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()




