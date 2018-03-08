#!/usr/bin/env python3
""" Models - data representation for WeConnect web application.

    Holds routines for users to interact wih the system (API).
"""
class Users(list):
    """ Holds methods for users.
    
        Attributes:
            all_users (list) : Holds all user information
            login_status (bool) : True/False flag
    """
    def __init__(self):
        self.all_users = []
        self.login_status = False
        pass

    def create_user_account(self, username, user_email, user_password):
        """ (Users, str, str, str) -> str

            Creates a user account.
        """

        #TODO:
        # Simple validation before creating acc. 
        # store user details in dict and append to all_users
        pass #TODO: Msg to user success/fail

    def user_login(self, username, password):
        """ (Users, str, str) -> str

            Logs in a registered user.
        """
        #TODO: authenticate credentials

        pass #TODO: Msg to user success/fail

    def user_logout(self):
        """ (Users) -> str

            Logs out a user.
        """
        pass #TODO: msg to user

    def password_reset(self, current_password, new_password):
        """ (Users, str, str) -> str

            Resets user password.
        """
        #TODO:
        # Simple validation before creating acc.
        # update users password
        pass #TODO: msg to user
    
class BusinessReviews(list):
    """ Holds methods for interacting with reviews. """
    def __init__(self):
        self.all_reviews = []
        pass
    
    def add_a_review(self, business_id, review_data):
        """ (BusinessReviews, int, str) -> str 

            Adds a review for a business.
        """
        # link business name to approp businessID
        pass # msg to user
    
    def get_all_reviews_for_a_business(self, business_id):
        """ (BusinessReviews, int) -> stdout

            Gets all reviews for a business.
        """
        pass # Print/return to screen

class BusinessProfiles(list):
    """ Holds methods for interacting with business profiles. """

    def __init__(self):
        self.all_business_profiles = []
        self.business_id_count = 1
        pass
    
    def register_a_business(self, business_name, business_description):
        """ (BusinessProfiles, str, str) -> str

            Registers a business.
        """
        #TODO: assign businessID on creation
        pass # msg to user success/fail
    
    def update_a_business(
            self, bussiness_id, new_business_name, new_business_description):
        """ (BusinessProfiles, str, str) -> str
        
            Updates a business profile.
        """
        pass # msg to user
    
    def remove_a_business(self, bussiness_id):
        """ (BusinessProfiles, int) -> str
        
            Removes a business profile.
        """
        pass # msg to user

    def retrieve_a_business_profile(self, business_id):
        """ (BusinessProfiles, int) -> stdout
        
            Retrieves a business profile.
        """
        pass # return/print to screen


    
        
    
