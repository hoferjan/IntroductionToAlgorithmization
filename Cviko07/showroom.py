class Car:
    def __init__(self, identification: int, name: str, brand: str, price: int,
                 active: bool):  # přijímá seznam (list) instancí třídy Car a na jejich základě vytvoří spojový seznam.
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active


class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None


db = LinkedList()


def init(cars):
    for item in cars:
        add(item)


def add(car):
    if db.head == None:
        db.head = Node(None, None, car)
        # print("Here comes the head")
    elif db.head.data.price > car.price:
        old_head = db.head
        db.head = Node(old_head, None, car)
        # print("new head came")
    else:
        # print(db.head.nextNode)
        tmp_node = db.head
        tmp_next_node = db.head.nextNode

        while True:
            if tmp_node.nextNode == None:
                # print("End of chain")
                tmp_node.nextNode = Node(None, tmp_node, car)
                break
            elif tmp_next_node.data.price > car.price:
                # print("price checks out")
                tmp_node.nextNode = Node(tmp_next_node, tmp_node, car)
                tmp_next_node.prevNode = Node(tmp_next_node, tmp_node, car)
                break
            else:
                tmp_node = tmp_node.nextNode
                tmp_next_node = tmp_next_node.nextNode


def updateBrand(identification: int, brand: str):  # Tohle prenest na dalsi dve funkce dle zadani, aby nehazeli error
    tmp_node = db.head
    while tmp_node != None:
        if tmp_node.data.identification == identification:
            tmp_node.data.brand = brand
            break
        else:
            tmp_node = tmp_node.nextNode
    return None


def updateName(identification: int, name: str):
    tmp_node = db.head
    while tmp_node != None:
        if tmp_node.data.identification == identification:
            tmp_node.data.name = name
            break
        else:
            tmp_node = tmp_node.nextNode
    return None


def activateCar(identification):
    tmp_node = db.head
    while tmp_node != None:
        if tmp_node.data.identification == identification:
            tmp_node.data.active = True
            break
        else:
            tmp_node = tmp_node.nextNode
    return None


def deactivateCar(identification):
    tmp_node = db.head
    while tmp_node != None:
        if tmp_node.data.identification == identification:
            tmp_node.data.active = False
            break
        else:
            tmp_node = tmp_node.nextNode
    return None


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    sum = 0
    tmp_node = db.head
    while True:
        if tmp_node.data.active == True:
            sum += tmp_node.data.price
        if tmp_node.nextNode == None:
            return sum
        tmp_node = tmp_node.nextNode


def clean():
    db.head = None


def printdb():
    tmp_node = db.head
    while tmp_node != None:
        print(
            f"identification :{tmp_node.data.identification}, name:{tmp_node.data.name}, brand:{tmp_node.data.brand}, price:{tmp_node.data.price}, active:{tmp_node.data.active}")
        tmp_node = tmp_node.nextNode

# clean()
# carList = []
# carList.append(Car(1, "Octavia", "Skoda", 123000, True))
# carList.append(Car(23, "Felicia", "Skoda", 5000, True))
# carList.append(Car(11, "Superb", "Skoda", 54000, True))

# carList.append(Car(1,"Fabia", "Skoda",1000000 , True))
# carList.append(Car(2,"X", "Tesla", 100000, True))
# carList.append(Car(3,"i8", "BMW",10000, True))
# carList.append(Car(4, "Benz", "Mercedes", 1000, True))
# carList.append(Car(5,"A8", "Audi", 1, True))
# carList.append(Car(6, "Splash", "Suzuki", 10, True))
# carList.append(Car(7, "Prius", "Toyota", 100, True))
#
# init(carList)
#
# printdb()
# print()
# #print(calculateCarPrice())

# deactivateCar(7)
# activateCar(7)
# updateBrand(7,"Hyundai")
# updateName(8,"Elantra")

# printdb()
# print()
# activateCar(7)
# printdb()

# print(getDatabaseHead())
# print(getDatabase())
# print(calculateCarPrice())
# printdb()
