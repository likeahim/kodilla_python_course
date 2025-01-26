import sys
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG, filename='calculator_logs.log')

logging.info("welcome in calulator")
def calculate():
    result = 0
    action = ""
    sign = input("""
    decide what do you want to do?
    1 divide
    2 multiply
    3 add
    4 subtract\n""")
    first_number = float(input("enter first number:\n"))
    second_number = float(input("enter second number:\n"))
    if sign == '1':
        result = first_number / second_number
        action = 'divide'
    elif sign == '2':
        result = first_number * second_number
        action = 'multiply'
    elif sign == '3':
        result = first_number + second_number
        action = 'add'
    elif sign == '4':
        result = first_number - second_number
        action = 'subtract'
    logging.info("chosen action is " + action)
    print("result is " + str(result))
    logging.debug("program ends with success")

if __name__ == '__main__':
    calculate()