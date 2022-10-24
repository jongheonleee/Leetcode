class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None for _ in range(k)]
        self.f = 0
        self.r = 0
        self.k = k


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.arr[self.r] = value
        self.r = (self.r+1)%self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        item, self.arr[self.f] = self.arr[self.f], None
        self.f = (self.f+1) % self.k
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.arr[self.f]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.arr[(self.r-1)%self.k]

    def isEmpty(self) -> bool:
        if self.f == self.r and self.arr[(self.f+1)%self.k] == None:
            return True
        
        return False

    def isFull(self) -> bool:
        return self.f == self.r and self.arr[self.f] != None

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()