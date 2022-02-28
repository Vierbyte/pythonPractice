

class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = int(age)
        self.grade = grade
        self.has_pc = True

    def no_pc(self):
        self.has_pc = False
        print(self.name + " has no computer.")