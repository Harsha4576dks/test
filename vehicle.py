class vehicle():
     def __init__(self):
          self.owner = "jagesh"
          print(f"The owner of the vehicle is {self.owner}")
    

class four_wheeler(vehicle):
     def __init__(self):
          super().__init__()
          self.brand = "toyota"
          self.model = "hybrid"
          self.fuel = "petrol"

          print(f"The brand name is {self.brand} and {self.model} model, with {self.fuel} variant")

class two_wheeler(vehicle):
     def __init__(self):
          super().__init__()
          self.brand = "suzuki"
          self.model = "2.0"       

          print(f"The brand name is {self.brand} and {self.model} model")


class six_wheeler(vehicle):
     def __init__(self):
          super().__init__()
          self.brand = "toyota"
          self.model = "hybrid"
          self.fuel = "petrol"

          print(f"The brand name is {self.brand} and {self.model} model, with {self.fuel} variant")

v1 = vehicle()
v2 = four_wheeler()
v3 = two_wheeler()
v4 = six_wheeler()