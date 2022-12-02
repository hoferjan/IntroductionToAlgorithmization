import car

class Node:
    def __init__(self, car):
        self.next = None
        self.car=car
class LinkedList:
        def __init__(self):
            self.head = None
        def push(self,car):
            new_node = Node(car)
            if self.head == None:
                self.head = new_node
            else:
                tmp_node = self.head
                while tmp_node != None:
                    tmp_node = tmp_node.next
                tmp_node.next = new_node
        def print_items(self):
            tmp_node = self.head
            while tmp_node != None:
                print(tmp_node.car)
                tmp_node = tmp_node.next
        def pop(self):
            #TODO pop from empty linked list
            car_to_return = self.head.car
            self.head = self.head.next
            pass



    ll = LinkedList()
    ll.push(car.Car("Porsche", 9328098))
    ll.push(car.Car("BMW", 4328098))
    ll.push(car.Car("Audi", 3529098))
    ll.push(car.Car("Tesla", 432328098))
    ll.push(car.Car("Mercedes", 40932488))