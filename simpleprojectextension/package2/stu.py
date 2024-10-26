class Student:
    def __init__(self, sid, sname, grad):
        self.sid = sid
        self.sname = sname
        self.grad = grad
    def Displaystu(self):
        print(self.sid, self.sname, self.grad)