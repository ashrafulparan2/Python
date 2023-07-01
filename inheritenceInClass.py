class Vehicle:
    def general_usage(self):
        print("general")


class Car(Vehicle):
    def __init__(self):
        print("car")
        self.wheels = 4
        self.roof = True

    def usage(self):
        print("spec_use")


class Moto(Vehicle):
    def __init__(self):
        print("moto")
        self.wheels = 4
        self.roof = True

    def usage(self):
        print("racing")


c = Car()
c.general_usage()
c.usage()

m = Moto()
m.general_usage()
m.usage()

print(isinstance(c, Car))
print(issubclass(Car, Vehicle))
