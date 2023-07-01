class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if (self.occupation == "tennis player"):
            print(self.name, "plays tennis")
        else:
            print(self.name, "does nothing")

    def speaks(self):
        print("hi")


tom = Human("Tom Cruise", "actor")
tom.speaks()
tom.do_work()
maria = Human("Maria", "tennis player")
maria.do_work()
