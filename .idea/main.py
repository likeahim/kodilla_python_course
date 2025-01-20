shopping_dict = {
    "piekarnia": ["bułki", "chleb", "mąka"],
    "lidl": ["mleko", "ser", "ręcznik papierowy"],
    "bierdronka": ["woda", "przekąski", "banany"],
    "wędkarski": ["wędka", "podbierak", "nosówki"]
}

for item in shopping_dict:
    products = [product.capitalize() for product in shopping_dict[item]]
    print(f"idę do {item.capitalize()} aby kupić {products}")
all_products = sum(len(values) for values in shopping_dict.values())
print(f"w sumie kupię {all_products} produktów")

print("what the change")
