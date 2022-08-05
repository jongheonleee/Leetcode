# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''if head is None:
            return None
        
        p1, p2 = head, head.next if head else None
        
        while p2:
            if p1.val == p2.val:
                p1.next = p2.next
                
            # p1, p2 = p1.next, p2.next.next
            if p2.next:
                p1, p2 = p1.next, p2.next.next
                
            else:
                p1, p2 = p1.next, None
            
            
        return head'''

        if head is None:
            return None
        
        p1, p2 = head, head.next if head else None
        
        while p2:
            if p1.val == p2.val:
                # most important thing is that i have to move p2 to p2.next
                # then, connect p1.next with p2
                p2 = p2.next
                p1.next = p2
                
            else:
                p1, p2 = p2, p2.next
            
            
        return head
                
        