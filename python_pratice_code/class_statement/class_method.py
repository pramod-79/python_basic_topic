# The class `Car` defines a car object with attributes for brand and model, and a method to display
# the full name of the car.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_full_name(self):
        return f"{self.brand} {self.model}"
        
my_car = Car("BMW", "M5")
print(my_car.display_full_name())