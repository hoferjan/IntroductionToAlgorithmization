import car

class Queue:
    def __init__(self):
        self.data =[]
    def push(self,item):
        if self.is_empty():
            self.data.append()
            return
        for i in range(len(self.data)):
            if item.price > self.data[i].price:
                self.data.insert(i,item)
                return
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop(0)
    def size(self):
        return len(self.data)
    def is_empty(self):
        return self.size == 0
    def print_items(self):
        for item in self.data:
            print(item)

my_queue = Queue()
my_queue.push(car.Car("Porsche",9328098))
my_queue.push(car.Car("BMW",4328098))
my_queue.push(car.Car("Audi",3529098))
my_queue.push(car.Car("Tesla",432328098))
my_queue.push(car.Car("Mercedes",40932488))

my_queue.print_items()

print(my_queue.pop())
print(my_queue.pop())
print(my_queue.pop())

