def customized_hello(name, surname, default_prefix='Mr'):
    print(f"Hello, {default_prefix} {name} {surname}!")

customized_hello('John', 'Doe')

customized_hello("Mary", "Jane", "Mrs")

#generic fuctions

shopping_items = [
    "jajka",
    "mleko",
    "bułka",
    "ser feta",
    "pomidor",
    "masło"
]

def shopping(items):
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart

basket = shopping(shopping_items)
print(basket)