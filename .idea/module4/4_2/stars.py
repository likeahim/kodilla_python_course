#one and two stars with args

def count_them_all(*args):
    print(args)
    print(f"received: {len(args)} arguments")

count_them_all(1,2,3,4,5,6,7,8,9, 'numbers')

def count_specifics(*args, **kwargs):
    print(f"positional: {len(args)} arguments")
    print(f"named: {len(kwargs)} arguments")

count_specifics(1,2,3,4,5,6,7,8,9, 'numbers', some='juju')