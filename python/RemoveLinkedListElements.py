# Question No. 203
# Remove Linked List Elements
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            if cur.val != val:
                if not prev:
                    head = cur
                prev = cur
            else:
                if prev:
                    prev.next = cur.next
            cur = cur.next
        if not prev:
            head = None
        return head