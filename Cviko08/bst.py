class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"value:{self.value}"


class BinarySearchTree:
    def __init__(self):
        self.head = None
        self.counter = 0

    def insert(self, value):
        self.counter = 0
        if self.head == None:
            self.head = Node(value)
            #print(f"head: {self.head}")
            return
        tmp_node = self.head
        while True:
            self.counter =+1
            if value < tmp_node.value:
                if tmp_node.left == None:
                    tmp_node.left = Node(value)
                    print(f"from {tmp_node} to left: {tmp_node.left}")
                    return
                tmp_node = tmp_node.left
                continue
            if value > tmp_node.value:
                if tmp_node.right == None:
                    tmp_node.right = Node(value)
                    #print(f"from {tmp_node} to right: {tmp_node.right}")
                    return
                tmp_node = tmp_node.right
                continue
            return

    def fromArray(self, array: list):
        for item in range(len(array)):
            self.insert(array[item])
        return

    def search(self, value) -> bool:
        self.counter = 0
        if self.head == None:
            return False
        tmp_node = self.head
        while True:
            self.counter +=1
            if value < tmp_node.value:
                if tmp_node.left == None:
                    return False
                if tmp_node == value:
                    return True
                tmp_node = tmp_node.left
                continue
            if value > tmp_node.value:
                if tmp_node.right == None:
                    return False
                if tmp_node == value:
                    return True
                tmp_node = tmp_node.right
                continue
            return True

    def min(self) -> int:
        self.counter = 0
        if self.head == None:
            return None
        tmp_min = self.head
        while True:
            self.counter+=1
            if tmp_min.left == None:
                return tmp_min.value
            else:
                tmp_min = tmp_min.left


    def max(self):
        self.counter = 0
        if self.head == None:
            return None
        tmp_max = self.head
        while True:
            self.counter+=1
            if tmp_max.right == None:
                return tmp_max.value
            else:
                tmp_max = tmp_max.right

    def visitedNodes(self):
        return self.counter


bst1 = BinarySearchTree()

bst1.fromArray([-4390, -8480, -1646, 1267, 7626, 1669, -4589, -4356, 5702, 1144])

