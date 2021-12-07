# Question No. 1290
# Convert Binary Number in a Linked List to Integer
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = head.val
        tmp = head.next
        while tmp:
            result <<= 1
            result += tmp.val
            tmp = tmp.next
        return result