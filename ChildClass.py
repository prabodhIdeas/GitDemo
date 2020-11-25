#inheritance
from OopsDemo import calculator


class childImpl(calculator):
    num2 = 200

    def __init__(self):
        calculator.__init__(self, 2, 7)

    def getcompletedata(self):
        return self.num2 + self.num + self.summation()

obj = childImpl()
print(obj.getcompletedata())