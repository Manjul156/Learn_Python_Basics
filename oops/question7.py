class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_discription():
        return "Cars are the main source of transport"

my_car = Car("toyta", "fortuner")
print(my_car.brand)
print(my_car.model)
print(my_car.general_discription())