#!/usr/bin/env python3
""" Tests for views.py """

from app import app
import json
import unittest

class SimpleTestCases(unittest.TestCase):
    """ Test cases """
    def setUp(self):
        # test client
        # Sample user data
        # Sample Business data
        # sample profile data
        # sample review data
        pass
    
    def test_register_user_http_response_status(self):
        # 201 & 404
        pass 
    
    def test_register_user_returns_operation_status_message(self):
        # Success/Fail
        pass
    
    def test_register_user_handles_invalid_input(self):
        # bad password (length)
        # taken username
        pass
    

    def test_login_http_response_status(self):
        # 201 & 404
        pass

    def test_login_returns_operation_status_message(self):
        # Success/Fail
        pass
    
    def test_logout_http_response_status(self):
        # 201 & 404
        pass
    
    def test_logout_returns_operation_status_message(self):
        # Success/Fail
        pass

    def test_register_business_http_response_status(self):
        # 201 & 404
        pass
    
    def test_register_business_returns_operation_status_message(self):
        # Success/Fail
        pass
    
    def test_password_reset_http_response_status(self):
        # 201 & 404
        pass

    def test_password_reset_returns_operation_status_message(self):
        # Success/Fail
        pass
    
    def test_update_a_business_http_response_status(self):
        # 405, 200, 204, 404
        pass

    def test_update_a_business_returns_operation_status_message(self):
        # Success/Fail
        pass
    
    def test_delete_a_business_http_response_status(self):
        # 405, 200, 404
        pass 
    
    def test_delete_a_business_returns_operation_status_message(self):
        # Success/Fail
        pass
    
    def test_display_all_businesses_http_response_status(self):
        # 200 & 404
        pass

    def test_display_a_businesses_http_response_status(self):
        # 200 & 404
        pass

    def test_add_a_review_returns_operation_status_message(self):
        # Success/Fail
        pass
    
    def test_add_a_review_http_response_status(self):
        # 200 & 404
        pass

    def test_display_all_businesses_returns_operation_status_message(self):
        # Success/Fail
        pass
    
    def test_display_all_businesses_http_response_status(self):
        # 200 & 404
        pass


    


    
if __name__ == '__main__':
    unittest.main()
