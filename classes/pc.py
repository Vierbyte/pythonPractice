from student import *
class PC:
    def __init__(self, btype, OS, ram):
        self.btype = btype
        self.OS = OS
        self.ram = ram
        self.is_on = False

    def power_on(self):
        self.is_on = True
        

    def pc_attributes(self):
        print("Student has a " + self.btype + " computer. The computer is running " + self.OS + " and has " + str(self.ram) + "GBs of ram.")

