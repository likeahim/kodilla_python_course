from car import Car
from business_card import BusinessCard

mustang = Car(make="Ford", model_name="Mustang", top_speed=270, color="blue")

print(mustang.make)


cards = []
cards.append(BusinessCard())
cards.append(BusinessCard())
cards.append(BusinessCard())

for card in cards:
    print(card)
    print(card.company)
    print(card.position)

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Fiesta", top_speed=200, color="Blue")
car_three = Car(make="Porsche", model_name="911", top_speed=320, color="Black")
cars = [car_one, car_two, car_three]
by_speed = sorted(cars, key=lambda car: -car.top_speed) #od najszybszego
by_make = sorted(cars, key=lambda car: car.make)

for car in by_make:
    print(car)
for car in by_speed:
    print(car)

by_first_name = sorted(cards, key=lambda card: card.first_name)
by_last_name = sorted(cards, key=lambda card: card.last_name)
by_email = sorted(cards, key=lambda card: card.email)

print("C A R D S")
print(by_first_name)
print(by_last_name)
print(by_email)

for card in cards:
    print(card.length_of_data)