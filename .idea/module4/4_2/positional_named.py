shopping_items = [
    "mleko",
    "bułki"
]

#named
def shopping(items, *, payment='cash', shop='local'):
    print(f"paying method: {payment} \nplace: {shop}")

#error
# shopping(shopping_items, 'card', shop='mall')

shopping(shopping_items, payment='card')

#positional
def shopping2(items, payment='cash', shop='local', /):
    print(f"paying method: {payment} \nplace: {shop}")

#error
# shopping2(shopping_items, payment='card')

shopping2(shopping_items, 'cash', 'mall')

#exercise
def fun_default(a='a', b='b'):
    print(a + b)

def fun_positional(a='a', b='b', /):
    print(a + b)

def fun_keyword(*, a='a', b='b'):
    print(a + b)

fun_default()
fun_positional('c', 'd')
fun_keyword(a='f', b='g')