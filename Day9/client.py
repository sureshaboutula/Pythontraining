#### Access module1 and module2 from pack1 package
#### Importing modules from a pckage


import sys
sys.path.append("C:/Users/0G3425649/Documents/Pythontraining/Day9/pack1")

####### Approach 1:
# import module1
# import module2

# module1.display()
# module2.show()

####### Approach 2: This approach will show some errors but ignore them as the program will work well
from module1 import *
from module2 import *

display()
show()