# Question No.725
# Split Linked List in parts
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head, k: int):
        list_len = 0
        temp = head
        while temp != None:
            list_len += 1
            temp = temp.next
        divide = list_len // k
        remains = list_len % k
        results = []

        for i in range(remains):
            results.append(head)
            for j in range(divide + 1):
                previous = head
                head = head.next
            previous.next = None

        for i in range(k - remains):
            if divide == 0:
                results.append(None)
            else:
                results.append(head)
                for j in range(divide):
                    previous = head
                    head = head.next
                previous.next = None

        return results