


class parent:
    ram = "Shri vishnu"
    def __int__(self):
        print("constructor of parent class")
    def method(self):
        print("Hello im from parent class")

class child(parent):
    def __int__(self):
        print("constructor of child class")
    def method1(self):
        print("loginpage child class")

c= child()
c.method()
c.ram
