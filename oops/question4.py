class Car:
    def __init__(self, __brand, model):
        self.__brand = __brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} : {self.model}"

my_car = Car("toyta", "fortuner")
# print(my_car.__brand)
print(my_car.model)

print(my_car.full_name())