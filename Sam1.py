class car:
    def __init__(self, speed, position):
        self.speed = speed
        self.position = position

    def car_forward(self, speed, position):
        speed += 10
        position += 10

    def car_reverse(speed, position):
        speed -= 10
        position -= 10


# Let's try those methods

car1 = car(0, 0)
car1.car_forward(10, 10)
print(car1.speed)
print(car1.position)
