# file one.py


a = 10

def func():
    print("func() in one.py")

print("top-level in one.py")
print("name of module - " + __name__)

if __name__ == '__main__':
    print("one.py is run directly")
else:
    print("one.py is being imported into another module")

