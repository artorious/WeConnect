#!/usr/bin/env python3

from app.models import WeConnect
import unittest

class TestWeConnectModel(unittest.TestCase):
    def setUp(self):
        self.tester = WeConnect()
    
    def test_WeConnet_inits_with_empty_dict(self):
        self.assertDictEqual({}, self.tester)

    def test_create_user_returns_user_info(self):
        sample = {'username': 'art', 'email': 'art@me', 'password':'123'}
        sample_test = self.tester.create_user(sample)
        self.assertDictEqual(sample, sample_test)

    def test_login_returns_user_info(self):
        sample_test = self.tester.login({'username': 'art','password':'123'})
        sample = {'username': 'art','password':'123'}
        self.assertDictEqual(sample, sample_test)
    
    def test_logout_returns_msg(self):
        sample_test = self.tester.logout()
        sample = "You are logged out"
        self.assertEqual(sample, sample_test)

    def test_register_business_returns_user_info(self):
        sample = {
            'username': 'art', 'business_name': 'dukani',
            'location': 'kabete', 'description': 'mama-ntilie'
        }
        sample_test = self.tester.register_business(sample)
        self.assertDictEqual(sample, sample_test)

    def test_reset_password_returns_success_msg(self):
        sample = {'password': '1234', 'new_password': '4321'}
        sample_test = self.tester.reset_password(sample)
        self.assertEqual('Success', sample_test)

    def test_reset_password_returns_failiure_msg(self):
        sample = {'password': None, 'new_password': '4321'}
        sample_test = self.tester.reset_password(sample)
        self.assertNotEqual('Password-reset failed', sample_test)

    def test_update_business_success_msg(self):
        sample = {
            'username': 'art', 'business_name': 'dukani',
            'location': 'kabete', 'description': 'mama-ntilie'
        }
        sample_test = self.tester.update_business(sample)
        self.assertDictEqual(sample, sample_test)

    def test_delete_business_operation_success(self):
        sample = {'username': 'art', 'business_name': 'dukani', 'location': 'kabete', 'description': 'mama-ntilie'}
        sample_test = self.tester.delete_business(sample)
        self.assertEqual('Deleted Successfully', sample_test)
    
        
if __name__ == '__main__':
    unittest.main()
    