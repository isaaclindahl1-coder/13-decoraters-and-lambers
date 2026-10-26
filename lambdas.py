#A lambda function in python is a small, anonymous function
#- anonymous means it has no name
# - usally it's run once and discarded (on the fly)
# Key facts about lambdas
# They can take any number of arguments
# They can contaion only one expresion (single line of code)
#They are commonly used  with *higher-order function* like map(), filter(), and reduce(), which are
#   functions that take other function as arguments

# Basic syntax:
# lambda parameters: expression
# eg. lamba x: x * 2

# Ex 1:
double = lambda x: x * 2
print(double(2)) # 4
print(double(3)) #6


add = lambda x, y: x +y

print(add(3,4)) #7
print(add(4,5)) #9

# max_value = lambda x,y: x if x > y else y
max_value = lambda x,y: x if x > y else y


print(max_value(4, 5))
print(max_value(9, 8))

#lambda function that exepets first and last name and returnes a user name 
# that is first inital , lastname, and the length (not counting num)
# eg. jason klins would be jklins6

user = lambda fn, ln: fn[0]+ln+str(len(fn[0]+ln))
 