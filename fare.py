class Vehicle:
    def __init__(self, seats):
        self.seats = seats

class Bus(Vehicle):
    def fare(self):
        return self.seats * 100

bus = Bus(50)

print("Total Fare:", bus.fare())