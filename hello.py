import sys


def main():
    #print sys.argv[0]
    #print sys.argv[1]
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = "World"
    print "Hello", name

if __name__ == '__main__':
    main()
