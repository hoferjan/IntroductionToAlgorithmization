lst = [15,19,10,7,17,16]

class Maxheap:

    def __init__(self,data):
        self.data = data

    def get_left_child_i(self,index):
        li = index * 2 + 1
        if li > len(self.data)-1:
            return None
        else:
            return li

    def get_right_child_i(self, index):
        ri = index * 2 + 2
        if ri > len(self.data)-1:
            return None
        else:
            return ri

    def sift_down(self, index):
        li = self.get_left_child_i(index)
        ri = self.get_right_child_i(index)
        tmp_max_i = index

        if li is not None and self.data[tmp_max_i] < self.data[li]:
            tmp_max_i =  li
        if ri is not None and self.data[tmp_max_i] < self.data[ri]:
            tmp_max_i = ri
        if tmp_max_i != index:
            self.data[tmp_max_i], self.data[index] = self.data[index], self.data[tmp_max_i]
            self.sift_down(tmp_max_i)

    def heapify(self):
        for i in range(len(self.data)-1, -1, -1):
            self.sift_down(i)
            print(self.data)

mh = Maxheap([15,19,10,7,17,16])
mh.heapify()


