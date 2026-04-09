class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        right, left = head, res

        for i in range(n):
            right = right.next

        while right is not None:
            left = left.next
            right = right.next

        left.next = left.next.next
        return res.next