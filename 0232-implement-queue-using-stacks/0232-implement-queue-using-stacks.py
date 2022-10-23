class MyQueue:
    def __init__(self):
        self.st1:list = []
        self.st2:list = []
    def push(self, x: int) -> None:
        self.st1.append(x)
        
    def move(self) -> None:
        while self.st1:
            self.st2.append(self.st1.pop())
            
        return None
        
    def pop(self) -> int:
        self.move()
        item = self.st2.pop()
        
        while self.st2:
            self.st1.append(self.st2.pop())
            
        return item

    def peek(self) -> int:
        self.move()
        item = self.st2.pop()
        self.st2.append(item)
        
        while self.st2:
            self.st1.append(self.st2.pop())
            
        return item

        

    def empty(self) -> bool:
        return True if len(self.st1) == 0 else False

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()