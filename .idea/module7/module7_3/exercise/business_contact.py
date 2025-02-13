from business_card import BusinessCard

class BusinessContact(BusinessCard):
    def __init__(self, business_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone = business_number