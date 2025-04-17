class Restaurant:
    """ Make a restaurant with name and cuisine type """
    def __init__(self, name, cuisine):
        """ Initialize name and cuisine type attributes. """
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """ Introduce about restaurant """
        print(f'The {self.name} is a {self.cuisine} restaurant')

    def set_number_serve(self,number_customers):
        self.number_served = number_customers

    def increment_number_served(self,customers):
        self.number_served += customers

    def display_number_customers(self):
        print(f'Restaurant {self.name} served {self.number_served} customers')

    def open_restaurant(self):
        print(f'Restaurant {self.name} is open now')