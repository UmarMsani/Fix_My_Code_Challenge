#!/usr/bin/python3
""" User class
"""

import bcrypt


class User:
    """ User class
    """
    def __init__(self, password):
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def is_valid_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password)
