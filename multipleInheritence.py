class father:
    def __init__(self):
        print("cons")
    def x(self):
        print("hi")
class mom:
    def __init__(self):
        print("moms")
    def y(self):
        print("hello")
        
class child(mom,father):
    def z(self):
        print("child")
        
        
c=child()
# c.x()
c.y()
c.z()
