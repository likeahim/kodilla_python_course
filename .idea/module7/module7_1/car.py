class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

    def __str__(self):
        return f'{self.make} {self.model_name} {self.top_speed} {self.color}'
