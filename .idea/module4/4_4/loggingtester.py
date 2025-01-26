import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

print("The program was called with this parameters %s" % sys.argv[1:])
print("the first parameter is %s" % sys.argv[1])
def print_naturity(age):
    if age >= 18:
        print("you are an adult")
    else:
        print("you are a kiddo")

if __name__ == '__main__':
    logging.debug("The program was called with this parameters %s" % sys.argv[1:])
    logging.debug("First parameter is %s" % sys.argv[1])