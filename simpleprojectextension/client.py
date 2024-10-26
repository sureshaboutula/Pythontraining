####### Approach 1 ###############
# import sys
# sys.path.append("C:/Users/0G3425649/Documents/Pythontraining/simpleprojectextension/package1")
# sys.path.append("C:/Users/0G3425649/Documents/Pythontraining/simpleprojectextension/package2")

# import emp
# Objemp = emp.Employee(101, "Scott", 5000)
# Objemp.Displayemp()

# import stu
# Objstu = stu.Student(201, "John", "A")
# Objstu.Displaystu()

########## Approach 2 ##########################
import sys
sys.path.append("C:/Users/0G3425649/Documents/Pythontraining/simpleprojectextension/package1")
sys.path.append("C:/Users/0G3425649/Documents/Pythontraining/simpleprojectextension/package2")

from emp import * ### We can write from emp import Employee also
from stu import Student

Objemp = Employee(101, "Scott", 5000)
Objemp.Displayemp()

Objstu = Student(201, "John", "A")
Objstu.Displaystu()
