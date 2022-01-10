class CQueue:

    def __init__(self):
        self.x = []

    def appendTail(self, value: int) -> None:
        self.x.append(value)

    def deleteHead(self) -> int:
        if len(self.x) == 0:
            return -1
        temp =  self.x[0]
        del self.x[0]
        return temp



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
