# The code defines a Car class with a display_full_name method and an Electric_Car subclass that
# inherits from Car and adds a battery_Size attribute.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_full_name(self):
        return f"{self.brand} {self.model} "
    
class Electric_Car(Car):
    def __init__(self, brand, model, battery_Size):
        super().__init__(brand, model)
        self.battery_Size = battery_Size

my_car = Electric_Car("OLA","zs","90kwh") 
print(my_car.brand)
print(my_car.model)
print(my_car.battery_Size)
print(my_car.display_full_name())