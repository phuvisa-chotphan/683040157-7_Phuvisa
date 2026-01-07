"""
Phuvisa Chotphan
683040157-7
P1
"""

from datetime import datetime, timedelta

class Cat:
    # Class attribute
    count = 0

    def __init__(self, in_name="N/A", in_breed="Unknown", in_age="Unknown", in_owner="N/A"):
        self.name = in_name
        self.breed = in_breed
        self.age = in_age
        self.owner = in_owner
        Cat.count += 1

        self.last_date_in = datetime.now()
        self.last_date_out = None
    
    # Instance methods
    def print_cat(self):
        print(f"----- Cat Record -----")
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Owner: {self.owner}")
        print(f"Age: {self.age}")
        print(">>>> Treatment record")
        print(f">>>> Last in: {self.last_date_in}")
        print(f">>>> Last out: {self.last_date_out}")
        print(f"----- End record -----")


    def greet(self):
        print(f"Meaw~ {self.name} =^.^=")

    def get_time_in(self):
        return self.last_date_in
    
    def get_time_out(self):
        return self.last_date_out
    
    def set_time_out(self, time=datetime.now()):
        self.last_date_out = time

    # Class methods
    @classmethod
    def get_num(cls):
        return cls.count
    
    @classmethod
    def reset_cat(cls):
        cls.count = 0


john = Cat("John","Thailand","2","Best")
pon = Cat("Pon",in_age="1")
alexander = Cat("Alexander","Macedonia","10","Macedonia")

print("===== First cat =====")
print(john.get_time_in())
john.greet()

print("===== Second cat =====")
pon.set_time_out()
print(pon.last_date_out)
pon.last_date_out = datetime.now() + timedelta(days=2)
print(pon.last_date_out)

print("===== Third cat =====")
print(alexander.owner)
alexander.owner = "I forgot"
print(alexander.owner)

#john.print_cat()
#pon.print_cat()
#alexander.print_cat()

print("-- using Cat.reset_cat --")
print(Cat.count)
Cat.reset_cat()
print(Cat.count)