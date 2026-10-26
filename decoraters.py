"""
A decirator in python is a function that extainds the behaivor of another function without modyfing it

- takes a base function as input
-Adds extra code or functionalyity before or after a function runs
-Returns a new function that combines both behaiors.
"""

#base function:
def get_ice_cream():
    print("Here is your ice cream")


# creat a simple decorater
# A decorater is just a function that takes another function as an argument
def add_sprinkles(func):
    #define a function that we will return (commonly called the wrapper)
    def wrapper():
        print("You add sprinkles")
        #call the function that was passed in:
        func()
    return wrapper #note we are not returning a result of wrapper, we are returning the function itself


# Base function with decorator:
#Decorator is applied with
@add_sprinkles
def get_ice_cream_decorated():
    print("Here is your ice cream")

#uodate this code to have  an add_fudge decorator


if __name__ == "__main__":
    get_ice_cream()