from faker import Faker

fake = Faker("pl_PL")

class BusinessCard:
    def __init__(self):
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.phone = fake.phone_number()
        self.email = fake.email()

        self._length_of_data = len(self.first_name) + len(self.last_name) + 1
    @property
    def length_of_data(self):
        return self._length_of_data

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.phone}'

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    def contact(self):
        return f"Dialing number {self.phone} and calling {self.first_name} {self.last_name}"
