# Positional and keyword (named) arguments in function usage example

# positional args
def calcSI(p, r, t):
    si = p * r * t
    return si


si = calcSI(100, 0.05, 1)
print("SI for {} yrs is {}".format(1, si))


# keyword/named args
def calcCI(p, r, t):
    return p * (1 + r) ** t


# ci = calcCI(p=200, r=0.05, t=2)
ci = calcCI(p=200, t=2, r=0.05)
print(ci)


# keyword args can also mean **kwargs
def printLangTypes(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} == {value}')


printLangTypes(Java="Platform Independent", C="System", Python="Interpreted")


# For explanation of below line see last section of this file
# printLangTypes(**{"Java": "Platform Independent", "Python": "Interpreted"})


# Similarly, *args is used to pass variable number of arguments to a function
# * next to args means - take rest of the parameters given and put them in a tuple called args
def printDaysOfWeek(*args):
    print(type(args))
    for arg in args:
        print(arg)


printDaysOfWeek("Mon", "Tue", "Wed")


# Parameter with default values
def powerOrSquare(num, pow=2):
    print(num ** pow)


# pow value in below call will default to 2 as it is not passed
powerOrSquare(5)
powerOrSquare(5, 3)


# One can pass *args to function call also.
# It means - take this list called args and unwrap it into rest of the parameters
def fun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Supports both list and tuple
# args=("Python", "is", "fun")
args = ["Python", "is", "fun"]
fun(*args)
# fun("python", "is", "fun")

# Similarly, **kwargs can be passed to function call
kwargs = {"arg1": "Python", "arg2": "is", "arg3": "fun"}
fun(**kwargs)


# Or
def morefun(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} == {value}')


morefun(**kwargs)
