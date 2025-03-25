"""
The class `Car` defines a blueprint for creating car objects with attributes for brand and model,
and an instance `my_car` is created with brand "BMW" and model "M5".
"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
my_car = Car("BMW", "M5")
print(my_car.brand)
print(my_car.model)
