class Employee:
    def __init__(self, eid, ename, salary):
        self.eid = eid
        self.ename = ename
        self.salary = salary
    def Displayemp(self):
        print(self.eid, self.ename, self.salary)
