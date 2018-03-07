#!/usr/bin/env python3
""" Models - data representation """

class WeConnect(dict):
    """ Holds methods for users, businesses and reviews """

    def __init__(self):
        """ Init """
        self.user_info = {}
        self.business_info = {}
        self.login_status = False
        self.logout_status = False


    def create_user_acc(self, username, user_email, user_password):
        """ Create User account """
        self.user_info = {'username': username, 'email': user_email, 'password': user_password}
        return self.user_info
        
    def login(self, username, user_password):
        """ Logs in a user """
        login_info = {'username': username,  'password': user_password}
        self.login_status = True
        return login_info
       
    
    def logout(self):
        """ Logs out a user """
        self.logout_status = True
        return "You are logged out"
        
    def reg_business(self, username, business_name, location, description):
        """ Register a business """
        self.business_info = {
            'username': username, 'business_name': business_name,
            'location': location, 'description': description
        }
        return self.business_info
# TODO:        
    def reset_password(self, current_password, new_password):
        """ Password reset """
        # returns
        pass
    

        