from business_card import BusinessCard

class BaseContact(BusinessCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)