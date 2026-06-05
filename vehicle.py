class vehicle:
    def __init__(self):
        self.owner = "jagesh"


class four_wheeler(vehicle):
    def __init__(self):
        super().__init__()
        self.brand = "toyota"
        self.model = "hybrid"
        self.fuel = "petrol"


class two_wheeler(vehicle):
    def __init__(self):
        super().__init__()
        self.brand = "suzuki"
        self.model = "2.0"


class six_wheeler(vehicle):
    def __init__(self):
        super().__init__()
        self.brand = "toyota"
        self.model = "hybrid"
        self.fuel = "petrol"


class output:
    def __init__(self):

        print("1: four_wheeler")
        print("2: two_wheeler")
        print("3: six_wheeler")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            v = four_wheeler()
            print(f"\nOwner: {v.owner}")
            print(f"This is a four wheeler of brand '{v.brand}' and model '{v.model}', with '{v.fuel}' variant")

        elif choice == 2:
            v = two_wheeler()
            print(f"\nOwner: {v.owner}")
            print(f"This is a two wheeler of brand '{v.brand}' and model '{v.model}'")

        elif choice == 3:
            v = six_wheeler()
            print(f"\nOwner: {v.owner}")
            print(f"This is a six wheeler of brand '{v.brand}' and model '{v.model}', with '{v.fuel}' variant")

        else:
            print("Invalid input")


# Create the menu object, no need off other object's to initialize
o = output()