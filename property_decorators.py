class Employee:
    def __init__(self, fname, sname):
        self.fname = fname
        self.sname = sname
    @property
    def fullname(self):
        return self.fname+" "+self.sname
    @property
    def email(self):
        return self.fname+"."+self.sname+"@gmail.com"
    @fullname.setter
    def fullname(self,name):
        fname, sname = name.split(" ")
        self.fname = fname
        self.sname = sname
    @fullname.deleter
    def fullname(self):
        self.fname = None
        self.sname = None

    @email.setter
    def email(self, email):
        dis = email.split(".")
        self.fname = dis[0]
        name = dis[1].split("@")
        self.sname = name[0]

e1 = Employee('Eddy', 'Kubwimana')
print(e1.fname)
e1.fname = "Eric"
print(e1.fullname)
e1.sname = "habonimana"
print(e1.email)
e1.fullname = "Eddy Ndihokubwayo"
print(e1.email)
print(e1.fullname)
del e1.fullname

e1.email = "steve.niyonkuru@gmail.com"
print(e1.email)
print(e1.fname)
print(e1.fullname)


