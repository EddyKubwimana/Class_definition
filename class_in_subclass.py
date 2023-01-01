class Employee:
    def __init__(self, fname, sname):
        self.fname = fname
        self.sname = sname
    def fullname(self):
        return self.fname+" "+self.sname
    def email(self):
        return self.fname+"."+self.sname+"@gmail.com"

class Developer(Employee):
    def __init__(self, fname, sname,prog_lang):
        super().__init__(fname,sname)
        self.prog_lang = prog_lang
    def qualification(self):
        return self.prog_lang
    def __str__(self):
         return f"Developer({self.fname}, {self.sname}, {self.prog_lang})"
class Manager(Employee):
    def __init__(self, fname, sname,employees = None):
        super().__init__(fname,sname)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self, employee):
       self.employees.append(employee)
    def remove_employee(self, employee):
       self.employees.remove(employee)

    def all_employees(self):
       return [(x.fullname(), x.email(), x.qualification()) for x in self.employees]
    
    def __str__(self):
        return f"Manager({self.fname}, {self.sname})"


e1 = Developer("Eddy","Kubwimana","python")
e2 = Developer("Didas", "Habonayo", "Java")

manager = Manager("Eric","habarugira",[e1,e2])
print(e1.qualification())
print(manager.all_employees())
print(e2)
print(manager)
