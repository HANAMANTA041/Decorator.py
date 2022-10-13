"""
#Use of decoration function
def decor_function(input_function):
    def inner():
        print("#"*10)
        print("Decoration with flowers")
        input_function()
        print("#"*10)
    return inner
@decor_function
def old_function():
    print("No decoration")

old_function()

#Use of decorater function(without use of decorator)
def decor_function(input_function):
    def inner():#wrapped function
        print("#"*10)
        print("Decoration with flowers")
        input_function()
        print("#"*10)
    return inner

def old_function():
    print("No decoration")

returned_function = decor_function()
returned_function(old_function)

#class decorater
class Mydecorater:
    def __init__(self,function):
        self.function = function

    def __call__(self):
        print("*"*10)
        self.function()
        print("*"*10)

@Mydecorater
def function():
    print("Banglore")
function()

class CheckDenom:
    def __init__(self,func):
        self.func = func

    def __call__(self,*args):
        if args[1] == 0:
            return "Denominator can't be zero"
        else:
            self.func(*args)
@CheckDenom
def div_function(x,y):
    print(x/y)

    div_fun = div_function(2,0)
    print(div_fun)
"""
