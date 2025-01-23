shopping_items = [
    "mleko",
    "bułki"
]

def shopping(items, payment='card', shop='local'):
    print(f"paying method: {payment} \nplace: {shop}")

shopping(shopping_items)
shopping(shopping_items, shop='square_circle_mall')
shopping(shopping_items, 'cash') #różne odniesienia do domyślnego parametru metody, przy zmianie, pozycyjne, albo nazwane