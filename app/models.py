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
        users (list):  Holds all the users information
        all_businesses_info: Holds business info about all registered businesses
    """

    def __init__(
            self, user_info={}, business_info={},
            login_status=False, reviews=[], users=[],
            all_businesses_info=[]
        ):
        self.user_info = user_info
        self.business_info = business_info
        self.login_status = login_status
        self.reviews = reviews
        self.users = users
        self.all_businesses_info = all_businesses_info
        self.updated_record = None

    def create_user(self, user_data):
        """ (WeConnect, dict) -> dict
        
            Create User account 
        """
        self.user_info = {
            'username': user_data.get('username'),
            'email': user_data.get('email'),
            'password': user_data.get('password')
        }
        self.users.append(self.user_info)
        return self.user_info
        
    def login(self, login_data):
        """ (WeConnect, dict) -> dict

            Logs in a user 
        """
        self.login_info = {
            'username': login_data.get('username'),
            'password': login_data.get('password')
        }
        self.login_status = True
        return self.login_info
       
    def logout(self):
        """ (WeConnect) -> str
        
            Logs out a user 
        """
        self.login_status = False
        return "You are logged out"

    def reset_password(self, password_data):
        """ (WeConnect, dict) -> str
            
            Password reset 
        """
        self.user_info['password'] = password_data.get('old_password')
        return 'Success'       

    def register_business(self, business_data):
        """ (WeConnect, dict) -> dict
        
            Register a business 
        """
        self.business_info = {
            'username': business_data.get('username'), 
            'business_name': business_data.get('business_name'),
            'location': business_data.get('location'), 
            'description': business_data.get('description')
        }
        self.all_businesses_info.append(self.business_info)
        return self.business_info

    def update_business(self, business_update_data):
        """ (WeConnect, dict) -> dict
         
            Updates business profile 
        """
        for business_entity in self.all_businesses_info:
            if business_entity['username'] == business_update_data.get('username'):
                business_entity.update(business_update_data)
                self.all_businesses_info.append(business_entity)
                self.updated_record = business_entity
                return updated_record
            
    def delete_business(self, business_name):
        """ (WeConnect, str) -> str
            
            Removes a business 
        """
        for business_entity in self.all_businesses_info:
            if business_name == self.business_entity.get(business_name):
                self.all_businesses_info.remove(business_entity)
        return 'Deleted Successfully'
     
    def list_all_businesses(self):
        """ (WeConnect) -> dict 
            
            Retrieves all business 
        """
        return self.all_businesses_info

    def list_a_single_business(self, business_name):
        """ (WeConnect, str) -> dict

            Retrieves a business profile 
        """
        for business_entity in self.all_businesses_info:
            if business_name == self.business_entity.get(business_name):
                return business_entity
     
    def add_a_review(self, review_data):
        """ (WeConnect, dict) -> str
        
            Add a review for a business 
        """
        self.reviews.extend(review_data)
        return 'Added Successfully'

    def list_all_reviews(self, business_name):
        """ (WeConnect, str) -> list
        
            Get all reviews for a business 
        """
        for review_item in self.reviews:
            if review_item.get(business_data) == business_name:
                temp_review_container = []
                temp_review_container.append(review_item)
        return temp_review_container

        
