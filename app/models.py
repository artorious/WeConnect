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
        
    def login(self, username, password):
        """ Logs in a user """
        # returns
        pass
    
    def logout(self):
        """ Logs out a user """
        # returns
        pass

# TODO:        
    # def reset_password(self, current_password, new_password):
    # 	""" Password reset """
    #     # returns 
    #     pass
    
    # def reg_business(self, business_name, location, description):
	# 	""" Register a business """
    #     # returns 
	# 	pass
        