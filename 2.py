# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        finish = result = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            result.next = ListNode(carry % 10)
            carry = carry // 10
            result = result.next
        return finish.next
        
Resh = Solution()
print(Resh.addTwoNumbers([2,4,3],[5,6,4]))
