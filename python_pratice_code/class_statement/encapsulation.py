class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_access(self):
        return self.__brand
    
    def display_full_name(self):
        return f"{self.__brand} {self.model}"

class Electric_Car(Car):
    def __init__(self, __brand, model, battery_Size):
        super().__init__(__brand, model)
        self.battery_Size = battery_Size
    
my_car = Car("tata","safari")
print(my_car.get_access())
print(my_car.display_full_name())


my_new_car = Electric_Car("bmw", "m5","50kwh")
print(my_new_car.get_access())
print(my_new_car.model)
print(my_new_car.display_full_name())