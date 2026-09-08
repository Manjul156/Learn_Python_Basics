class Car:
    def __init__(self, __brand, model):
        self.__brand = __brand
        self.model = model

    @property
    def brand(self):
        return self.__brand

my_car = Car("toyta", "fortuner")
print(my_car.brand)
print(my_car.model)
