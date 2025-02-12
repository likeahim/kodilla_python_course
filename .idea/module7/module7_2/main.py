from car import Car

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
print(car.current_speed)

car.accelerate()
print(car.current_speed)
car.accelerate(50)
print(car.current_speed)

car.current_speed = 50
print(car.current_speed)
