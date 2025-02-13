from truck import Truck
from car import Car

truck = Truck(make='Mercedes', model_name='Actros', color='Black', top_speed='90', max_load='1200')
print(truck)
truck.accelerate()
print(truck.current_speed)

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="red")

print(isinstance(car, Car))
print(isinstance(car, Truck))
print(isinstance(truck, Car))

print(issubclass(Car, Truck))
print(issubclass(Truck, Car))
