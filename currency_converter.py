class currency:
    def __init__(self):
       
       self.rates = {
                "USD":1,
                "INR":90,
                "EUR":0.87,
                "GBP":0.75,
                "YEN":162,
                "AUD":1.43
            }

class conversion(currency):
    def __init__(self, amount, from_currency, to_currency):
        super().__init__()

        if  from_currency.upper() ==  to_currency.upper():
            print("They both are the same currencies")
        
        else:
            USD_converter = amount / self.rates[from_currency.upper()]
            self.converted_amount = USD_converter * self.rates[to_currency.upper()]
      
    def show_result(self):
        print(f"The conversion value of your amount is {self.converted_amount}")
        
       
amount = float(input("Enter amount:"))
from_currency = input("Enter from_currency:")
to_currency = input("Enter to_currency:")
        
converter = conversion(amount, from_currency, to_currency)
converter.show_result()