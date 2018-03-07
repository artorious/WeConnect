#!/usr/bin/env python3
""" Models - data representation """

class WeConnect(dict):
    """ Holds methods for users, businesses and reviews """

    def __init__(self):
        """ Init """
        self.user_info = {}

    def create_user_acc(self, username, user_email, user_password):
        """ Create User account """
        self.user_info = {'username': username, 'email': user_email, 'password': user_password}
        return self.user_info
        
    def login(self, username, user_password):
        """ Logs in a user """
        login_info = {'username': username,  'password': user_password}
        return login_info
       
    
    def logout(self):
        """ Logs out a user """
        return "You are logged out"
       

# TODO:        
    # def reset_password(self, current_password, new_password):
    # 	""" Password reset """
    #     # returns 
    #     pass
    
    # def reg_business(self, business_name, location, description):
	# 	""" Register a business """
    #     # returns 
	# 	pass
        