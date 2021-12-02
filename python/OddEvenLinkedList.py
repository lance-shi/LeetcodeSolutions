# Question No. 328
# Odd Even Linked List
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        is_even = False
        even = even_head = head.next
        odd = head
        tmp = head.next.next
        while tmp:
            if not is_even:
                odd.next = tmp
                odd = tmp
            else:
                even.next = tmp
                even = tmp
            is_even = not is_even
            tmp = tmp.next
        odd.next = even_head
        even.next = None
        return head