class Car:
    add_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.add_car += 1
        
    def get_access(self):
        return self.__brand
    
    def display_full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or disel"
    
    @staticmethod
    def general_dec():
        return " This is a petrol car"
        

class Electric_Car(Car):
    def __init__(self, __brand, model, battery_Size):
        super().__init__(__brand, model)
        self.battery_Size = battery_Size
    
    def fuel_type(self):
        return "Electric battery"
    
    @staticmethod
    def general_dec():
        return" This is a Electric car" 
        
my_car = Car("tata", "safari")
print(my_car.general_dec())

my_new_car = Electric_Car.general_dec()
print(my_new_car)