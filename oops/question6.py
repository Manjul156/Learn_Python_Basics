class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.brand} : {self.model}"

my_car = Car("toyta", "fortuner")
my_car1 = Car("toyta", "fortuner")
my_car2 = Car("toyta", "fortuner")
print(my_car.brand)
print(my_car.model)

print(my_car.full_name())
print(my_car.total_car)