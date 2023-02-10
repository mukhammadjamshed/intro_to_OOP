class Car:
    def __init__(self, name: str, color: str, speed: int):
        self.name = name
        self.color = color
        self.speed = speed

    def __str__(self) -> str:
        return f"The speed of the {self.color} {self.name} car is {self.speed}"

if __name__ == '__main__':
    car1 = Car("Lacetti", "white", 220)
    car2 = Car("Malibu", "white", 260)
    car3 = Car("Matiz", "gray", 180)

    print(car1)
    print(car2)
    print(car3)
