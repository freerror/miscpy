class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, year, fname, lname):
        super().__init__(fname, lname)
        self.year = year

    def printname(self):
        super().printname()
        print(f"Graduated {self.year}")
    
    def welcome(self):
        print(f"Welcome {self.fname} {self.lname} to the class of {self.year}.")

x = Student(2019, "Mike", "Olsen")
x.printname()
x.welcome()