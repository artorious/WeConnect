#!/usr/bin/env python3

from app import app

import unittest

class SimpleTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_index_http_method(self):
        response = self.app.get('/v1/')
        self.assertIn('GET', str(response.data))

    def test_index_http_response_status(self):
        response = self.app.get('/v1/')
        self.assertEqual(200, response.status_code)
    
    
    def test_register_http_method(self):
        response = self.app.post("/v1/register")
        self.assertEqual('POST', str(response.data))
    
    def test_register_http_response_method(self):
        response = self.app.post("/v1/register")
        self.assertEqual(200, response.status_code)
    
    def test_register_returns_required_data(self):
        response = self.app.post("/v1/register")
        self.assertIn('username', response.data)
        self.assertIn('email', response.data)
        self.assertIn('password', response.data)


if __name__ == '__main__':
    unittest.main()



