class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        if head:
            curr = head
            
            while curr is not None:
                right = curr.next
                curr.next = prev
                prev = curr
                curr = right

        return prev