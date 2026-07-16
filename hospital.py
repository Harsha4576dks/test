Doctors = [
    {"name":"sundar", "specialization":"cardiologist", "available":True},
    {"name":"kamal", "specialization":"neurologist", "available":True},
    {"name":"skanda", "specialization":"gynaecologist", "available":False},
    {"name":"suma", "specialization":"dermatologist", "available":False}
]
class Hospital():
    def __init__(self, doctors):
        self.doctors = doctors

    def check_availability(self, name):
        for doctor in self.doctors:
            if doctor["name"].lower() == name.lower():
               return doctor["available"]
        return None

hospital = Hospital(Doctors)
name = input("Enter doctor name:")

is_available = hospital.check_availability(name)

if is_available is True:
    print(f"Dr. {name} is available")
elif is_available is False:
    print(f"Dr. {name} is not available")
else:
    print("Doctor not found in database")