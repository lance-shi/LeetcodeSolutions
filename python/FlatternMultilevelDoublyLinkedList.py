# Question No. 430
# Flattern a Multilevel Doubly Linked List
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        beginning, tail = self.get_flattern(head)
        return beginning

    def get_flattern(self, head):
        last = head
        keep_head = head
        while head != None:
            last = head
            if head.child != None:
                child_head, child_tail = self.get_flattern(head.child)
                temp = head.next
                head.child = None
                head.next = child_head
                child_head.prev = head
                child_tail.next = temp
                if temp:
                    temp.prev = child_tail
                last = child_tail
                head = temp
            else:
                head = head.next
        return (keep_head, last)