class Queensolver:

    def __init__(self, size):
        self.size = size
        self.board = [-1] * size

    def winner(self):
        pass #TODO

    def can_place(self, row):
        pass #TODO

    def place_queen(self, row):
        if row == self.size:
            return
        for column in range(self.size):
            if self.can_place(row,column):
                self.board[row] = column  # place queen
                if row == self.size-1:
                    self.winner()
                self.place_queen(row + 1)
                self.board[row] = -1 #remove queen

qs = Queensolver(4)

qs.place_queen(0)
