class Vehicle:

    def __init__(self, name ,  maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage


class bus(Vehicle):
    pass

schoolbus = bus("School volvo",180 , 12)
print('Vehicle name:', schoolbus.name ,  "speed", schoolbus.maxspeed, "mileage:", schoolbus.mileage)