class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def description(self):
        return f"{super().description()}, Battery: {self.battery_size} kWh"

# Example usage
car = Car("Toyota", "Camry", 2022)
ecar = ElectricCar("Tesla", "Model 3", 2023, 75)
print(car.description())
print(ecar.description())
