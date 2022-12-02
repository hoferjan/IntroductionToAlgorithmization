import car

class Stack:
    def __init__(self):
        self.data =[]

    def push(self,item):
        self.data.append(item)
    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()
    def size(self):
        return len(self.data)
    def is_empty(self):
        return self.size == 0
    def print_items(self):
        for item in self.data:
            print(item)

my_stack = Stack()
my_stack.push(car.Car("BMW",4328098))
my_stack.push(car.Car("Porsche",9328098))
my_stack.push(car.Car("Audi",3529098))
my_stack.push(car.Car("Tesla",432328098))
my_stack.push(car.Car("Mercedes",40932488))

my_stack.print_items()

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

