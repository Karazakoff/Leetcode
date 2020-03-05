class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(ListNode):
    def __init__(self):
        super.__init__(self.x)
    def getDecimalValue(self, head):
        exponent = 0
        decimal = 0
        values = [head.val]

        while (head.next):
            head = head.next
            exponent = exponent + 1
            values.append(head.val)

        for i in range(exponent+1):
            decimal = decimal + values[i] * 2 ** exponent
            exponent = exponent - 1

        return decimal

Resh = Solution([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
print(Resh.getDecimalValue())
