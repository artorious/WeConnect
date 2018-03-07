#!/usr/bin/env python3
""" Tests for views.py """


from app import app
import json
import unittest

class SimpleTestCases(unittest.TestCase):
    """ Test cases """
    def setUp(self):
        self.app = app.test_client()
        self.test_user = {'username': 'art', 'email': 'art@here', 'password': '1223'}
        self.test_biz = {'username': 'art', 'business_name': 'dukani', 'location': 'kabete', 'description': 'mama-ntilie'}
    
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

    def test_login_http_response_status(self):
        response = self.app.post("/v1/login/", data=json.dumps(self.test_user), headers={'content-type': 'application/json'})
        self.assertEqual(201, response.status_code)
    
    def test_login_returns_required_data(self):
        response = self.app.post("/v1/login/", data=json.dumps(self.test_user), headers={'content-type': 'application/json'})
        self.assertIn('username', str(response.data))
        self.assertIn('password', str(response.data))
    
    def test_logout_returns_approp_msg(self):
        logout_msg = 'You are logged out'
        response = self.app.post("/v1/logout/", data=json.dumps(logout_msg), headers={'content-type': 'application/json'})
        self.assertIn('You are logged out', str(response.data))

    def test_register_biz_http_response_status(self):
        response = self.app.post("/v1/businesses/", data=json.dumps(self.test_biz), headers={'content-type': 'application/json'})
        self.assertEqual(201, response.status_code)
    
    def test_register_biz_returns_required_data(self):
        response = self.app.post("/v1/businesses/", data=json.dumps(self.test_biz), headers={'content-type': 'application/json'})
        self.assertIn('username', str(response.data))
        self.assertIn('business_name', str(response.data))
        self.assertIn('location', str(response.data))
        self.assertIn('description', str(response.data))


if __name__ == '__main__':
    unittest.main()



