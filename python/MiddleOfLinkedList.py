# Question No. 876
# Middle of the linked list
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n_list = []
        tmp = head
        while tmp:
            n_list.append(tmp)
            tmp = tmp.next
        n = len(n_list)
        return n_list[n // 2]