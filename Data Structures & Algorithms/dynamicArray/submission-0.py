class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.currentArraySize = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size + 1 > self.currentArraySize : 
            self.resize()
        self.array[self.size] = n 
        self.size += 1

    def popback(self) -> int:
        temp = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return temp

    def resize(self) -> None:
        newArray = [0] * (2*self.currentArraySize)
        for idx , val in enumerate(self.array) :
            newArray[idx] = val
        self.array = newArray
        self.currentArraySize *= 2 
            
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.currentArraySize
