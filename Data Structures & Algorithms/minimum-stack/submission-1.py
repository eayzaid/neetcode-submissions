class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        topElement = self.getMin()
        if val <= topElement : 
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        topElement = self.getMin()
        topElementMain = self.stack.pop()
        if topElement == topElementMain : 
            self.minStack.pop()

    def top(self) -> int:
        num = self.stack.pop()
        self.stack.append(num)
        return num
    
    def getMin(self) -> int:
        if not self.minStack :
            topElement = 2**31 - 1
        else : 
            topElement = self.minStack.pop()
            self.minStack.append(topElement)
        return topElement

        
