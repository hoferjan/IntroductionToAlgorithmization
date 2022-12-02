class Car:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def __str__(self):
        return f"brand :{self.brand}, price:{self.price}"

