cars = ["Ford", "Audi", "Alfa Romeo", "Skoda", "Toyota" ]

class Collection:

    def __init__(self,list):
        self.list =list

    def print_items(self):
        for item in range(len(self.list)):
            print("Znacka je "+ self.list[item])

    def contains_item(self,item):
        for i in range(len(self.list)):
            if item == self.list[i]:
                return True
        return False

    def add_item(self,item):
        if self.contains_item(item) == True:
            return None
        else:
            self.list.append(item)

    def revert_items(self): #dodelat
        self.list = self.list[::-1]

my_collection = Collection(cars)


my_collection.add_item("Tesla")

my_collection.print_items()

my_collection.revert_items()

my_collection.print_items()

