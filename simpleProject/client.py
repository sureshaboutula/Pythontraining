#### Approach 1:
# import sys
# sys.path.append("C:/Users/0G3425649/Documents/Pythontraining/simpleProject/package1")

# import module1
# module1.display()

# # import module2
# # module2.show()  ### ModuleNotFoundError: No module named 'module2' --> Module2 is not inside package1

# sys.path.append("C:/Users/0G3425649/Documents/Pythontraining/simpleProject/package1/package2")
# import module2
# module2.show()

#### Approach 2:
# import sys
# sys.path.append("C:/Users/0G3425649/Documents/Pythontraining/simpleProject/package1")
# sys.path.append("C:/Users/0G3425649/Documents/Pythontraining/simpleProject/package1/package2")

# from module1 import *
# from module2 import *

# display()
# show()

