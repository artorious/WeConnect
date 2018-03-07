#!/usr/bin/env python3
""" Models (data representation) for WeConnect web application """

class WeConnect(dict):
    """ Holds methods for CRUD users, businesses and reviews
    
    Attributes:
        user_info (dict) : A dictionary that holds user information.
        business_info (dict) : A dictionary that holds businesses 
                                information and profiles.
        
        login_status (bool): A boolean value that indicates whether the 
                                user is logged in or not (True/False).
        reviews (dict): A dictionary that holds all the reviews for all 
                            businesses
    """
    
    __user_info = {}
    __business_info = {}
    __login_status = False
    __reviews = {}
    __login_info = {}

    def __init__(
            self, user_info={}, business_info={},
            login_status=False, reviews={}
        ):
        self.__user_info = user_info
        self.__business_info = business_info
        self.__login_status = login_status
        self.__reviews = reviews

    def create_user(self, user_data):
        """ Create User account """
        self.__user_info = {
            'username': user_data.get('username'),
            'email': user_data.get('email'),
            'password': user_data.get('password')
        }
        return self.__user_info
        
    def login(self, login_data):
        """ Logs in a user """

        self.__login_info = {
            'username': login_data.get('username'),
            'password': login_data.get('password')
        }
        self.__login_status = True
        return self.__login_info
       
    def logout(self):
        """ Logs out a user """
        self.__login_status = False
        return "You are logged out"
        
    def register_business(self, business_data):
        """ Register a business """
        self.__business_info = {
            'username': business_data.get('username'), 
            'business_name': business_data.get('business_name'),
            'location': business_data.get('location'), 
            'description': business_data.get('description')
        }
        return self.__business_info

        
    def reset_password(self, password_data):
        """ Password reset """
        self.__user_info['password'] = password_data.get('old_password')
        return 'Success'

    def update_business(self, business_update_data):
        """ Updates business profile """
        self.__business_info['username'] = business_update_data.get('username')
        self.__business_info['business_name']\
            = business_update_data.get('business_name')
        self.__business_info['location'] = business_update_data.get('location')
        self.__business_info['description']\
            = business_update_data.get('description')
        return self.__business_info