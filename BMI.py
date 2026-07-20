class BMI():
    def __init__(self,):
        self.weight = None
        self.height = None

    def add_mass(self):
        print("welcome  to BMI calculator")
        self.weight = float(input("Enter your weight in kg's:"))
        choice = input("do you want to enter your height in meter? (y/n):").lower()
        if choice =="y":
            self.height = float(input("Enter your height in meter's:"))
        else:
            feet = int(input("enter your height in feet:"))
            inches = float(input("enter your height in inches:"))
            self.height = (feet * 0.3048) + (inches * 0.0254)
        
    def calculate_mass(self):
        BMI = self.weight / (self.height ** 2)
        print(f"your BMI is:{BMI:.2f}")
        
        while True:
            if BMI < 18.5:
                print("underweight")
                break
            elif  18.5 <= BMI <24.9:
                print("normal weight")
                break
            elif 25<= BMI <29.5:
                print("overweight")
                break
            else:
                print("obese")
                break
         
c1 = BMI()
c1.add_mass()
c1.calculate_mass()
