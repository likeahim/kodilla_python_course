class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

        self._current_speed = 0
    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")

    def set_speed(self, speed):
        self._current_speed = speed

    def accelerate(self, step=10):
        self._current_speed += step

    def decelerate(self, step=10):
        if self._current_speed > 0:
            self._current_speed -= step

    def __str__(self):
        return f'{self.make} {self.model_name} {self.top_speed} {self.color}'