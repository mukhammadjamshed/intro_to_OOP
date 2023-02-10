class Phone:
    def __init__(self, name: str, color: str, price: float):
        self.name = name
        self.color = color
        self.price = price

    def setName(self, name: str):
        self.name = name

    def getName(self) -> str:
        return self.name

    def setColor(self, color: str):
        self.color = color

    def getColor(self) -> str:
        return self.color

    def setPrice(self, price: float):
        self.price = price

    def getPrice(self) -> float:
        return self.price

    def getInfo(self) -> str:
        return f"Phone information:\nName: {self.name}\nColor: {self.color}\nPrice: ${self.price}"

if __name__ == '__main__':
    phone1 = Phone("Iphone", "black", 1000)
    phone2 = Phone("Redmi", "white", 150)

    print(phone1.getInfo())
    print("\n")
    print(phone2.getInfo())
