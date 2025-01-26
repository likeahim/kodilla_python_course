import sys

def customized_hello(firstname, lastname):
    print('Hello, %s %s' % (firstname, lastname))

if __name__ == '__main__':
    # print(sys.argv[1:])
    customized_hello(sys.argv[1], sys.argv[2])

#z zabezpiczeniem

def customized_hello2(first_name, last_name, prefix):
    print("Hello %s %s %s!" % (prefix, first_name, last_name))

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("prefix is needed")
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    prefix = sys.argv[3]
    customized_hello2(first_name, last_name, prefix)