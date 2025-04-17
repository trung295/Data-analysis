class User:
    """ Define an user """
    def __init__(self, first_name, last_name):
        """ Initilize a first name and last name attributes """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0

    def increment_login_attempts(self,number_login_attemps):
        self.login_attempts += number_login_attemps

    def reset_login_attemps(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f'User full name is: {self.first_name} {self.last_name}')


    def greet_user (self):
        print(f'Greeting {self.first_name} {self.last_name}')

