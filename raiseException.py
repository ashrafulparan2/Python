class accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def printt(self):
        print(self.msg)
        
try:
    raise accident("accident")
except accident as e:
    e.printt()
    
    
def process_file():
    try:
        f=open("D://Misc//Python//test.txt")
        x=1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("clean")
        f.close()    