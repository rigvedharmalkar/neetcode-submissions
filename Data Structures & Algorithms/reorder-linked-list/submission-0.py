# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Phase 1 - find the point to reverse

        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Phase 2 - reverse the second part
        second = slow.next
        prev = None
        slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Phase 3 - reorder the list
        first, second = head, prev

        while second:
            tmp1 = first.next
            tmp2 = second.next # 5 -> 6 -> None

            first.next = second
            second.next = tmp1  # 0 -> 6 -> 1 -> 2 -> 3 -> None

            first = tmp1
            second = tmp2 

            






        
        

        

        