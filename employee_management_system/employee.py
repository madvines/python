class Employee():
    def __init__(self, fn, ln, slry, grp):
        self.fn = fn
        self.ln = ln
        self.slry = slry
        self.grp = grp

class Manager(Employee):
    def __init__(self, fn, ln, slry, grp):
        super().__init__(fn, ln, slry, grp)
    
dan = Employee("Dan","Smith",50000,"SysAd")

mark = Manager("Mark","Candor",80000,"Eng")
