import sys

print("The program was called with this parameters %s" % sys.argv[1:])
print("the first parameter is %s" % sys.argv[1])
def print_naturity(age):
    if age >= 18:
        print("you are an adult")
    else:
        print("you are a kiddo")

if __name__ == '__main__':
    age = int(sys.argv[1])
    print_naturity(age)