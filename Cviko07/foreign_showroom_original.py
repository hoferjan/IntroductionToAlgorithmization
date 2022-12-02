class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = nextNode
        self.prevNode = prevNode
        if prevNode:
            prevNode.nextNode = self  ## toto je broken
        if nextNode:
            nextNode.prevNode = self
        self.data = data

        pass


class LinkedList:
    def __init__(self):
        self.head = None
        pass


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active
        pass


db = LinkedList()


def init(cars):
    for carIter in cars:
        add(carIter)
    #     if(not db.head):
    #         db.head = Node(None,None,carIter)
    #         continue

    #     while(db.head.prevNode):
    #         db.head = db.head.prevNode

    #     nodePos=db.head

    #     if(nodePos.nextNode):## auto>hlava
    #         while carIter.price >= nodePos.data.price:    # najdi drazsi auto
    #             if(not nodePos.nextNode):
    #                 Node(nodePos,None,carIter) ## nase auto je nejdrazsi
    #             nodePos = nodePos.nextNode

    #             ## kod je dobre jen potrebuju aby na sebe ukazovaly
    #         Node(nodePos,nodePos.nextNode,carIter)

    #         while(db.head.prevNode):
    #             db.head = db.head.prevNode

    #     else:
    #         Node(nodePos,None,carIter)


def add(car):
    if (not db.head):
        db.head = Node(None, None, car)
        return

    if db.head.data.price > car.price:
        db.head = Node(db.head, None, car)
        return

    nodePos = db.head
    nextNodePos = db.head.nextNode
    while db:
        if (nodePos.nextNode == None):
            Node(None, nodePos, car)
            return
        elif nextNodePos.data.price > car.price:  # najdi drazsi auto a vloz pred nej
            ##STOP and keep car here
            Node(nextNodePos, nodePos, car)
            return
        else:  ## Iterate
            nextNodePos = nextNodePos.nextNode
            nodePos = nodePos.nextNode


def updateName(identification, name):
    curAutoNode = db.head
    while curAutoNode is not None:
        if (curAutoNode.data.identification == identification):
            curAutoNode.data.name = name
            return curAutoNode
        curAutoNode = curAutoNode.nextNode
    return None


def updateBrand(identification, brand):
    curAutoNode = db.head
    while curAutoNode is not None:
        if (curAutoNode.data.identification == identification):
            curAutoNode.data.brand = brand
            return curAutoNode
        curAutoNode = curAutoNode.nextNode
    return None


def activateCar(identification):
    curAutoNode = db.head
    while curAutoNode is not None:
        if (curAutoNode.data.identification == identification):
            curAutoNode.data.active = True
            return curAutoNode
        curAutoNode = curAutoNode.nextNode
    return None


def deactivateCar(identification):
    curAutoNode = db.head
    while curAutoNode is not None:
        if (curAutoNode.data.identification == identification):
            curAutoNode.data.active = False
            return curAutoNode
        curAutoNode = curAutoNode.nextNode
    return None


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    totalPrice = 0
    if (db.head):
        curAutoNode = db.head
    else:
        return totalPrice
    while db:
        if (curAutoNode.data.active == True):
            totalPrice += curAutoNode.data.price
        if curAutoNode.nextNode == None:
            return totalPrice
        curAutoNode = curAutoNode.nextNode


def clean():
    db.head = None
    pass

def printdb():
    tmp_node = db.head
    while tmp_node != None:
        print( f"identification :{tmp_node.data.identification}, name:{tmp_node.data.name}, brand:{tmp_node.data.brand}, price:{tmp_node.data.price}, active:{tmp_node.data.active}")
        tmp_node = tmp_node.nextNode

carList = []
carList.append(Car(1,"Octavia", "Skoda", 123000, True))
carList.append(Car(23,"Felicia", "Skoda",5000 , True))
carList.append(Car(11, "Superb", "Skoda", 54000, True))
carList.append(Car(1,"Octavia", "Skoda", 68165, True))
carList.append(Car(23,"Felicia", "Skoda",798278 , True))
carList.append(Car(11, "prvniskoda", "prvniskoda", 23453, True))
carList.append(Car(11, "druhaskoda", "druhaskoda", 23453, True))

init(carList)
printdb()
# # clean()
# print(calculateCarPrice())

# add(Car(23, "Octavia", "Skoda", 123000,False))
# print(updateName(25,"yourmum"))
# add(Car(213, "FELIC", "Skoda", 88888,False))
# add(Car(211, "SUPER", "Skoda", 5410,False))

# print(getDatabase())
# print(getDatabaseHead())


# print(calculateCarPrice())

# # updateBrand(213,"ABCNEWBRAND")
# # print(updateName(213,"NEWNAME"))

# # deactivateCar(23)
# # deactivateCar(213)

# # activateCar(23)
# # print("carprice is ")
# # calculateCarPrice()

# # clean()

# print("not stuck")
# ##felicia ukazuje prevnode: supreb