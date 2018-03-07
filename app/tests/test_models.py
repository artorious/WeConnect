#!/usr/bin/env python3

from app.models import WeConnect
import unittest

class TestWeConnectModel(unittest.TestCase):
    def setUp(self):
        self.tester = WeConnect()
    
    def test_WeConnet_inits_with_empty_dict(self):
        self.assertDictEqual({}, self.tester)

    def test_create_user_acc_returns_user_info(self):
        sample_test = self.tester.create_user_acc('art', 'art@me',  '123')
        sample = {'username': 'art', 'email': 'art@me', 'password':'123'}
        self.assertDictEqual(sample, sample_test)

    def test_login_returns_user_info(self):
        sample_test = self.tester.login('art', '123')
        sample = {'username': 'art','password':'123'}
        self.assertDictEqual(sample, sample_test)
    
    def test_logout_returns_msg(self):
        sample_test = self.tester.logout()
        sample = "You are logged out"
        self.assertEqual(sample, sample_test)

if __name__ == '__main__':
    unittest.main()