"""Helicopter class"""


class Helicopter:
    def __init__(self, name, model, year, weight, type, price, engine_model="", ttsn=0):
        self.name = name
        self.model = model
        self.year = year
        self.total_weight = weight
        self.passenger_or_caro = type
        self.engine_model = engine_model
        self.price = price
        self.total_time_since_new = ttsn

    def take_off(self):
        print("---------------Taking of---------------")
        print("First, open the throttle slowly until you reach proper operating RPM.")
        print("Pull the collective gradually up. ")
        print("The helicopter is leaving the ground and you'll be able to use the cyclic.")
        print("You’ve taken off, slightly release forward cyclic pressure.")

    def landing(self):
        print("---------------Landing---------------")
        print("You are around 200–500 feet (61.0–152.4 m) above ground")
        print("You approached the edge of the landing area")
        print("Keep moving forward")
        print("Check that your parking brake is armed and then reduce all power.")

    def get_info(self):
        print("---------------Characteristics---------------")
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Weight: {self.total_weight}")
        print(f"Type: {self.passenger_or_caro}")
        print(f"Price: {self.price}")
        print(f"Engine model: {self.engine_model}")
        print(f"TTSN: {self.total_time_since_new}")


euro_copter = Helicopter("Euro copter", "EC 135 P3", 2010, 3180, "Cargo", 1896142, "PW206B2", 1740)
euro_copter.get_info()
euro_copter.take_off()
euro_copter.landing()
