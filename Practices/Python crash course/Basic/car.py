class Car:
    """ Create a car blueprint """
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.odometer = 0
        
    def describe_car(self):
        """ Return a full information """
        print(f'The car is {self.name} {self.model} {self.year}')

    def update_odometer(self,mileage):
        """ return update mileage """
        """ reject change if it attempts to roll back the odometer """
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('You can not roll back odometer')
     
    def read_odometer(self):
        """ print a statement showing car meleage """
        print(f"The car's mileage is {self.odometer}")