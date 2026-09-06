class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol or Disel"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_car = ElectricCar("tesla", "model 5", "100mKW")
your_car = Car("toyta", "fortuner")

print(my_car.brand)
print(my_car.model)
print(my_car.battery_size)
print(my_car.fuel_type())
print(your_car.fuel_type())
