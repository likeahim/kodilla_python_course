def sum_digits(a, b):
    sum = a + b
    print(sum)
print(type(sum_digits))
sum_digits(1, 2)

a = 1

def scope_demo():
    a = 2
    print(a)

scope_demo()
print(a)

def shopping():
    shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"
    ]
    shopping_cart = "Koszyk zawiera: `\n"
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart

print(shopping())

#multireturn
def day_times():
    return "morning", "afternoon", "evening", "night"

times = day_times()
print(times)
print(type(times))

first, second, third, fourth = day_times()
print("Trzeci element to %s" % third)