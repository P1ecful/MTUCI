class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def get_info(self):
    return(f"Марка: {self.make}, Модель: {self.model}")

class Car(Vehicle):
  def __init__(self, make, model, fuel):
    super().__init__(make, model)
    self.fuel = fuel
  
  def get_info(self):
    print(f"{super().get_info()}, Топливо: {self.fuel}")

newCar = Car("Nissan", "Skyline r34", "АИ-95")
newCar.get_info()