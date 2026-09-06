class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_car = ElectricCar("tesla", "model 5", "100mKW")
print(my_car.brand)
print(my_car.model)
print(my_car.battery_size)
