from business_card import BusinessCard
from base_contact import BaseContact
from business_contact import BusinessContact
from faker import Faker

fake = Faker("pl_PL")

def create_contact(contact, number):
    cards = []
    for number in range(0, number):
        if contact=="base":
            cards.append(BaseContact())
        else:
            number = fake.phone_number()
            cards.append(BusinessContact(business_number=number))
    return cards

business_cards = create_contact("business", 5)
base_cards = create_contact("base", 5)

print("BASE CARDS")
for card in base_cards:
    print(card)
    print(card.contact())

print("BUSINESS CARDS")
for card in business_cards:
    print(card)
    print(card.contact())
