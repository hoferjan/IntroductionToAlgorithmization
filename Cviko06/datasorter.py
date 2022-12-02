import random

class DataSorter:

    def __init__(self, item_count: int, from_num:int, to_num:int) ->None: #specifikace navratove hodnoty pres ->
        self.data: list[int] = []
        for i in range(item_count):
            self.data.append(random.randint(from_num,to_num))

    def __str__(self) -> str:
        result: str = ""
        for item in self.data:
            result +=(str(item) + " ")
        return result

    def swap(self,x:int,y:int) -> None:
        self.data[x], self.data[y] = self.data[y], self.data[x]

    def max(self) -> int:
        self.max=0
        for num in self.data:
            if num > self.max:
                self.max=num
        return self.max

    def bubble_sort(self):
        for j in range(len(self.data)):
            for i in range(len(self.data)-1-j):
                if self.data[i] > self.data[i+1]:
                    self.swap(i,i+1)
    def selection_sort(self):
        for first_unsorted_index in range(len(self.data)-1):
            min_index = first_unsorted_index
            for i in range (first_unsorted_index,len(self.data)):
                if self.data[i] < self.data[min_index]:
                    min_index=i
            self.swap(min_index,first_unsorted_index)


x=DataSorter(10,1,1000)
print(x.data)
print(x.data)
print(x.data)
print(x.data)
#x.bubble_sort()
x.selection_sort()
print(x.data)



