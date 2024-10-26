####### Invoking animal and bird modules in this module #############
#### Approach 1:

# import animal
# animal.fly()
# animal.color()

# # bird.fly() ### bird module is not imported
# # bird.color()  ### bird module is not imported

# import bird
# bird.fly()
# bird.color()

#### Approach 2:
# from animal import *
# from bird import *

# fly()  # Bird can fly
# color()  #Bird color is green
##### When same functions are present in imported modules, latest module functions will be invoked

###Remedy:
# from animal import *

# fly()  # Animal cannot fly
# color()  #Animal color is black

# from bird import *

# fly()  # Bird can fly
# color()  #Bird color is green