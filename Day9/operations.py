#### You cannot invoke below functions because they are different module
# add(100,200)
# mul(10,20)

##### To invoke functions from different module, use import

####### Approach 1 ###############
# import calculator
# calculator.add(100,200)
# calculator.mul(10,20)

######## Approach 2 ############
# from calculator import add,mul
# add(50,100)
# mul(5,10)

############## Approach 3 ###########
from calculator import * ### * will consider all functions and classes from selected module
add(50,100)
mul(5,10)