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

    def test_register_http_response_status(self):
        response = self.app.post("/v1/register/", data=json.dumps(self.test_user), headers={'content-type': 'application/json'})
        self.assertEqual(201, response.status_code)
    
    def test_register_returns_required_data(self):
        response = self.app.post("/v1/register/", data=json.dumps(self.test_user), headers={'content-type': 'application/json'})
        self.assertIn('username', str(response.data))
        self.assertIn('email', str(response.data))
        self.assertIn('password', str(response.data))


if __name__ == '__main__':
    unittest.main()



