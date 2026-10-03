# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Phase 1 - Reverse the list

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Phase 2 - Counter
        counter = 2
        if n == 1:
            prev = prev.next
        
        else:
            first = prev
            second = prev.next
            while counter != n:
                second = second.next
                counter += 1
            while first.next != second:
                first = first.next
            first.next = second.next
            second.next = None
        
        # Phase 3 - reverse again
        prev2 = None
        while prev:
            tmp = prev.next
            prev.next = prev2
            prev2 = prev
            prev = tmp
        return prev2

        
        
        

        
        

            