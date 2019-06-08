##Functions are defined outside classes
def iamfunction():
    print("inside function")
    return 1

##Methods are defined in class
class C:
    def __init__(self):
        print("In class constructor")
    def testmethod(self):
        print("in test method of class C")
        return 2


a = "test1"
b = "test2"
if __name__ == "__main__":
    iamfunction()
    c = C()
    print(c.testmethod())


