#!/usr/bin/env python3

from app.models import WeConnect
import unittest

class TestWeConnectModel(unittest.TestCase):
    def setUp(self):
        self.tester = WeConnect()
    
    def test_WeConnet_inits_with_empty_dict(self):
        self.assertDictEqual({}, self.tester)

    def test_create_user_acc_returns_user_info(self):
        sample_test = self.tester.create_user_acc('art@me', 'art', '123')
        sample = {'username': 'art', 'email': 'art@me', 'password':'123'}
        self.assertDictEqual(sample, sample_test)


if __name__ == '__main__':
    unittest.main()